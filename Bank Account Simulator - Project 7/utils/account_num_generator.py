import random

def generate_account_number():
    """ Generate a 10 digit unique account number"""
    random_number = str(random.randint(1000000000, 9999999999))
    return random_number

def generate_unique_account_number(existing_numbers):
    """ Generate a unique 10 digit account number not in existing_numbers """
    while True:
        account_number = generate_account_number()
        if account_number not in existing_numbers:
            return account_number