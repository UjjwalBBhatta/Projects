def validate_amount(amount):
    """"Validates transaction amount is a positive number."""
    try:
        amount = float(amount)
        if amount <= 0:
            return False, "Amount must be positive."
        return True, amount
    except ValueError:
        return False, "Invalid amount format."
    
def validate_account_exists(account_number, existing_accounts):
    """Check if the account number exists in the existing accounts."""
    if account_number in existing_accounts:
        return True, "Account number exists."
    return False, "Account number does not exist."

def validate_credentials(account_number, password, account_data):
    """Validate account number and password against stored account data."""
    if account_number in account_data:
        if account_data[account_number]['password'] == password:
            return True, "Login successful."
        else:
            return False, "Invalid password."
    return False, "Account number does not exist."

def validate_transfer(account_from, account_to, amount, existing_accounts):
    """Validate transfer details."""
    if account_from not in existing_accounts:
        return False, "Source account does not exist."
    if account_to not in existing_accounts:
        return False, "Destination account does not exist."
    is_valid_amount, amount_or_msg = validate_amount(amount)
    if not is_valid_amount:
        return False, amount_or_msg, "Insufficient funds."
    return True, amount_or_msg