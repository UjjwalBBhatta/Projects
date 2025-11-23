import json
from src.tracking import track_habits
from src.user_habits import user_habits
from src.user_inputs import handle_user_command
def main():
    print("Welcome to the Daily Habit Tracker!")
    while True:
        try:
            with open("menu.json", "r") as f:
                menu_data = json.load(f)
                print("\nMain Menu:")
                for command, description in menu_data.get("menu", {}).items():
                    print(f" - {command}")

            command = input("Please enter a command from the menu (or type 'exit' to quit): ").strip().lower()
            if command == "exit":
                print("Exiting the Daily Habit Tracker. Goodbye!")
                break
            handle_user_command(command)
        except FileNotFoundError:
            print("menu.json file not found.")
            break   
        except json.JSONDecodeError:
            print("Error decoding JSON from menu.json.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
if __name__ == "__main__":
    main()




