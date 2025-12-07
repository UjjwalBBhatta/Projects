import random
import string

def generate_password(length=16, use_symbols=True):
    """Generate a random password"""
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    
    return ''.join(random.choice(chars) for _ in range(length))