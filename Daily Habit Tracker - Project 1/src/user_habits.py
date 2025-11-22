import json
from . import custom_habits
def user_habits():
    """This module is used to let the user add or delete habits to track.
    The habits will be stored in the habits.json file.
    """
    with open("habits.json", "r") as f:
        data = json.load(f)
        if not data.get("tracking"):
            data["tracking"] = []
    action = input("Do you want to add or delete a habit? (add/delete): ").strip().lower()
    if action == "add":
        with open("habits.json", "r") as f:
            data = json.load(f)
            print("Available habits to add:")
            available_habits = set(data.get("default", []) + data.get("custom", [])) - set(data.get("tracking", []))
            if not available_habits:
                print("No available habits to add. You can add custom habits.")
            else:
                for habit in available_habits:
                    print(f" - {habit}")
        choice = input("Enter the name of the habit you want to add or type 'custom' to add a custom habit: ").strip().lower()
        if choice in available_habits:
            data["tracking"].append(choice)
            with open("habits.json", "w") as f:
                json.dump(data, f, indent = 4)
            print(f"The habit {choice} has been successfully added to your tracking list.")
        elif choice == "custom":
            custom_habits.custom_habits()
        else:
            print(f"The habit {choice} is not available to add.")
    elif action == "delete":
        habit = input("Enter the name of the habit that you want to delete: ").strip().lower()
        if habit in data.get("tracking", []):
            data["tracking"].remove(habit)
            with open("habits.json", "w") as f:
                json.dump(data, f, indent = 4)
            print(f"The habit {habit} has been successfully deleted.")
        else:
            print(f"The habit {habit} does not exist in the tracking list.")
    else:
        print("Invalid action. Please enter 'add' or 'delete'.")


