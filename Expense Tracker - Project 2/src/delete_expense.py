import json

def delete_expense():
    """This module provides functionality to delete an expense entry from the expenses.json file.
    It prompts the user for the date and description of the expense to be deleted."""
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return
    except json.JSONDecodeError:
        print("Error reading expenses data.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    date_str = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    description = input("Enter the description of the expense to delete: ")
    initial_count = len(expenses)
    expenses = [expense for expense in expenses if not (expense['date'] == date_str and expense['description'] == description)]
    if len(expenses) == initial_count:
        print("No matching expense found to delete.")
    else:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("Expense deleted successfully.")