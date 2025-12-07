from cryptography.fernet import Fernet
import base64
import os

def get_key():
    """Get or create encryption key"""
    if os.path.exists('data/key.key'):
        with open('data/key.key', 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open('data/key.key', 'wb') as f:
            f.write(key)
        return key

def encrypt_password(password):
    """Encrypt a password"""
    key = get_key()
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()