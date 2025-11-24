import json
from datetime import datetime, timedelta
def timeframe_expense():
    """This function calculates and displays the total expenses for a singular day or an user-defined timeframe.
    However we will have a cap upto how long the user can see the expenses (50 days).
    It reads the expenses from the expenses.json file and sums up the amounts for the specified date range.
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
    choice = input("Do you want to see expenses for a (1) Single Day or (2) Timeframe? Enter 1 or 2: ")
    if choice == '1':
        date_str = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
        if not date_str:
            date_str = datetime.now().strftime('%Y-%m-%d')
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        total_for_day = sum(expense['amount'] for expense in expenses if expense['date'] == date_str)
        print(f"Total expenses for {date_str}: ${total_for_day:.2f}")
        if total_for_day == 0:
            print("No expenses recorded for this day.")
        else:
            print("Here are the expenses for this day:")
            for expense in expenses:
                if expense['date'] == date_str:
                    print(f"- {expense['category']}: ${expense['amount']:.2f} ({expense['description']})")
    elif choice == '2':
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY_MM_DD): ")
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        if start_date > end_date:
            print("Start date cannot be after end date.")
            return
        if (end_date - start_date).days > 50:
            print("Timeframe cannot exceed 50 days.")
            return
        total_for_timeframe = sum(expense["amount"] for expense in expenses if start_date_str <= expense["date"] <= end_date_str)
        print(f"Total expenses from {start_date_str} to {end_date_str}: ${total_for_timeframe:.2f}")
        if total_for_timeframe == 0:
            print("No expenses recorded for this timeframe.")
        else:
            print("Here are the expenses for this timeframe:")
            for expense in expenses:
                if start_date_str <= expense["date"] <= end_date_str:
                    print(f"- {expense['date']} | {expense['category']}: ${expense['amount']:.2f} ({expense['description']})")
    else:
        print("Invalid choice. Please enter 1 or 2.")

