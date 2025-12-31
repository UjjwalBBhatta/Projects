import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TRANSACTIONS_DIR = os.path.join(DATA_DIR, 'transactions') 
ACCOUNTS_FILE = os.path.join(DATA_DIR, 'accounts.json')

def _ensure_data_dir_exists():
    """Internal helper: Makes sure data folders exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(TRANSACTIONS_DIR):
        os.makedirs(TRANSACTIONS_DIR)

def load_data(file_path):
    """Generic loader."""
    if not os.path.exists(file_path):
        return {} 
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {} 

def save_data(file_path, data):
    """Generic saver."""
    _ensure_data_dir_exists() 
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False


def add_transaction(account_id, amount, category, description=""):
    """
    Saves a transaction to a specific file: data/transactions/{account_id}_transactions.json
    """
    filename = f"{account_id}_transactions.json"
    file_path = os.path.join(TRANSACTIONS_DIR, filename)
    

    transactions = load_data(file_path)
    
    if isinstance(transactions, dict) and not transactions:
        transactions = []
        
    new_entry = {
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "amount": amount,
        "category": category,
        "description": description
    }
    
    transactions.append(new_entry)
    save_data(file_path, transactions)