import json
from datetime import datetime

def daily_expense():
    """This function calculates and displays the total expenses for the current day.
    It reads the expenses from the expenses.json file and sums up the amounts for today's date.
    """
    try:
        with open ("expenses.json", "r") as file:
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
    today_str = datetime.now().strftime('%Y-%m-%d')
    total_today = sum(expense['amount'] for expense in expenses if expense['date'] == today_str)
    print(f"Total expenses for today ({today_str}): ${total_today:.2f}")
    if total_today == 0:
        print("No expenses recorded for today.")
    else:
        print("Here are the expenses for today:")
        for expense in expenses:
            if expense['date'] == today_str:
                print(f"- {expense['category']}: ${expense['amount']:.2f} ({expense['description']})")  
    
