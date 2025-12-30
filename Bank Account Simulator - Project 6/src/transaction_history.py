import json
from datetime import datetime

def add_transaction(amount, category, description=""):
    """ This function adds a new transaction entry to the transactions.json file. 
    It prompts the user for transaction details and saves them in JSON format.
    It stores the date, amount, category, and description of the transaction.
    """
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []
    except json.JSONDecodeError:
        transactions = []
    date_str = datetime.now().strftime('%Y-%m-%d')
    transaction_entry = {
        "date": date_str,
        "amount": amount,
        "category": category,
        "description": description
    }
    if not all([date_str, amount, category]):
        print("All fields are required. transaction not added.")
        return
    transactions.append(transaction_entry)
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=4)
    print("Transaction recorded.")