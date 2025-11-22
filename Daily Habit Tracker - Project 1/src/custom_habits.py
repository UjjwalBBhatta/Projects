import json

def custom_habits():
    """This module is for adding custom habits.
    Users can define their own habits in addition to the default ones.
    The custom habits will be stored in a separate list within the habits.json file.
    """
    habit = input("Enter the name of the habit that you want to add: ").strip().lower()
    if not habit:
        print("Habit name cannot be empty.")
        return
    try:
        with open("habits.json", "r") as f:
            data = json.load(f)
        if habit in data.get("default", []) or habit in data.get("custom", []):
            print(f"The habit {habit} allready exists.")
            return
        data.setdefault("custom", []).append(habit)
        with open("habits.json", "w") as f:
            json.dump(data, f, indent=4)
            print(f"The habit {habit} has been successfully added")
    except FileNotFoundError:
        print("habits.json file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from habits.json.")
    except Exception as e:
        print(f"An error occured: {e}")

    


    
