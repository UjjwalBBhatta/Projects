import json
import sys

# Import your modules
# Ensure these files exist in the same directory!
import add_receiver
import del_receiver 
import create_content  
import send_email      

def load_menu():
    """Loads menu options from JSON file."""
    try:
        with open('menu.json', 'r') as f:
            data = json.load(f)
            return data['menu_options']
    except FileNotFoundError:
        print("❌ Error: menu.json not found!")
        return {}

def exit_app():
    print("Goodbye! 👋")
    sys.exit()

# --- THE COMMAND MAP ---
# Keys match the JSON keys. Values are the functions to run.
COMMAND_FUNCTIONS = {
    "1": add_receiver.add_receiver_interactive,
    "2": del_receiver.del_receiver, # Ensure your del_receiver has an interactive mode or handles input!
    "3": create_content.create_interactive,
    "4": send_email.send_bulk_emails_interactive,
    "q": exit_app
}

def handle_user_input():
    menu = load_menu()
    
    while True:
        print("\n" + "="*30)
        print("   📧 EMAIL BOT DASHBOARD")
        print("="*30)
        
        # Display Menu
        for key, desc in menu.items():
            print(f" [{key}] {desc}")
            
        choice = input("\nSelect an option: ").strip().lower()
        
        # Execute Command
        action = COMMAND_FUNCTIONS.get(choice)
        
        if action:
            try:
                action() # Calls the function
            except Exception as e:
                print(f"❌ An error occurred executing that command: {e}")
            
            # Pause so the user can read the result before the menu clears/reloads
            input("\nPress Enter to continue...")
        else:
            print("❌ Invalid command. Please try again.")

if __name__ == "__main__":
    handle_user_input()