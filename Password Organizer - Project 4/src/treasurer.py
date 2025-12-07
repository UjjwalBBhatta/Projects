import json
import os
from encryptor import encrypt_password
from decryptor import decrypt_password

STORAGE_FILE = 'data/passwords.json'

def load_passwords():
    """Load stored passwords"""
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_passwords(passwords):
    """Save passwords to file"""
    with open(STORAGE_FILE, 'w') as f:
        json.dump(passwords, f, indent=2)

def add_password(service, username, password):
    """Add a new password"""
    passwords = load_passwords()
    encrypted = encrypt_password(password)
    passwords[service] = {
        'username': username,
        'password': encrypted
    }
    save_passwords(passwords)

def get_password(service):
    """Retrieve a password"""
    passwords = load_passwords()
    if service in passwords:
        entry = passwords[service]
        decrypted = decrypt_password(entry['password'])
        return entry['username'], decrypted
    return None, None

def list_services():
    """List all stored services"""
    passwords = load_passwords()
    return list(passwords.keys())

def delete_password(service):
    """Delete a password"""
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        return True
    return False