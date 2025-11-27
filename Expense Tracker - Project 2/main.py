import json
from src.user_input import handle_user_input

def main():
    """Main function to run the expense management application.
    It prompts the user for commands and handles them accordingly.
    """
    print("Welcome to the Expense Management Application!")
    try:
        with open("menu.json", "r") as f:
            menu_data = json.load(f)
    except FileNotFoundError:
        print("Menu file not found. Exiting application.")
        return
    except json.JSONDecodeError:
        print("Error reading menu data. Exiting application.")
        return
    while True:
        print("\nAvailable Commands:")
        for command, description in menu_data.get("menu", {}).items():
            print(f"- {command}: {description}")
        user_command = input("Please enter a command: ").strip().lower()
        handle_user_input(user_command)
        if user_command == 'exit':
            print("Exiting the application. Goodbye!")
            break
if __name__ == "__main__":
    main()


    