import json
from datetime import date as dt
from . import user_habits

def track_habits():
    """This module is used to track the user's habits.
    It will take simple yes and no inputs for each habit the user is tracking.
    The tracking data will be stored in the tracking.json file with the date.
    """
    today = dt.today().isoformat()
    try:
        with open("habits.json", "r") as f:
            habit_data = json.load(f)
            tracking_habits = habit_data.get("tracking", [])
            if not tracking_habits:
                answer = input("Do you want to add habits to track? (yes/no): ").strip().lower()
                if answer in ["yes", "y"]:
                    user_habits.user_habits()
                    with open("habits.json", "r") as f:
                        habit_data = json.load(f)
                        tracking_habits = habit_data.get("tracking", [])
                elif answer in ["no", "n"]:
                    userInput = input("No habits tracking. Do you want to exit? (yes/no): ")
                    if userInput in ["yes", "y"]:
                        print("Exiting the habit tracker.")
                        return
                    else:
                        user_habits.user_habits()
                        with open("habits.json", "r") as f:
                            habit_data = json.load(f)
                            tracking_habits = habit_data.get("tracking", [])
            else:
                userinput = input("Do you want to add or delete habits before tracking? (add/delete/no): ").strip().lower()
                if userinput == "add" or userinput == "delete":
                    user_habits.user_habits()
                    with open("habits.json", "r") as f:
                        habit_data = json.load(f)
                        tracking_habits = habit_data.get("tracking", [])
        tracking_data = {}
        for habit in tracking_habits:
            while True:
                response = input(f"Did you complete the habit '{habit}' today? (yes/no): ").strip().lower()
                if response in ["yes", "y"]:
                    tracking_data[habit] = True
                    break
                elif response in ["no", "n"]:
                    tracking_data[habit] = False
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        try:
            with open("tracking.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data[today] = tracking_data
        with open("tracking.json", "w") as f:
            json.dump(data, f, indent=4)
            print("Your habit tracking for today has been saved.")
    except FileNotFoundError:
        print("Habits.json file not found. Please set up your habits first.")
    except json.JSONDecodeError:
        print("Error decoding JSON from habits.json.")
    except Exception as e:
        print(f"An error occurred: {e}")


