from cryptography.fernet import Fernet
from encryptor import get_key

def decrypt_password(encrypted_password):
    """Decrypt a password"""
    key = get_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()