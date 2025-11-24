import json
from datetime import datetime

def add_expense():
    """ This function adds a new expense entry to the expenses.json file. 
    It prompts the user for expense details and saves them in JSON format.
    It stores the date, amount, category, and description of the expense.
    """
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        expenses = []
    date_str = input("Enter the date of the expense (YYYY-MM-DD) or leave blank for today: ")
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    try:
        amount = float(input("Enter the amount of the expense: "))
    except ValueError:
        print("Invalid amount: Please enter a numeric value.")
        return
    category = input("Enter the category of the expense (e.g., Food, Transport, Utilities): ")
    description = input("Enter a brief description of the expense: ")
    expense_entry = {
        "date": date_str,
        "amount": amount,
        "category": category,
        "description": description
    }
    if not all([date_str, amount, category, description]):
        print("All fields are required. Expense not added.")
        return
    if amount <= 0:
        print("Amount must be a positive number. Expense not added.")
        return
    expenses.append(expense_entry)
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    print("Expense added successfully.")
