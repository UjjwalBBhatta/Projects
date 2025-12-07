from src.outputs import display_menu, display_password, display_services, display_message
from src.user_inputs import get_menu_choice, get_service_name, get_username, get_password
from src.treasurer import add_password, get_password as retrieve_password, list_services, delete_password
from src.generator import generate_password
from src.strength_checker import check_strength

def main():
    """Main program loop"""
    
    print("Welcome to Password Manager!")
    
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == '1':
            # Add password
            service = get_service_name()
            username = get_username()
            password = get_password()
            strength = check_strength(password)
            
            display_message(f"Password strength: {strength}")
            confirm = input("Save this password? (y/n): ")
            
            if confirm.lower() == 'y':
                add_password(service, username, password)
                display_message(f"Password saved for {service}!")
        
        elif choice == '2':
            # Retrieve password
            service = get_service_name()
            username, password = retrieve_password(service)
            
            if password:
                strength = check_strength(password)
                display_password(service, username, password, strength)
            else:
                display_message(f"No password found for {service}")
        
        elif choice == '3':
            # List services
            services = list_services()
            if services:
                display_services(services)
            else:
                display_message("No passwords stored yet")
        
        elif choice == '4':
            # Generate password
            length = int(input("Password length (default 16): ") or "16")
            password = generate_password(length)
            strength = check_strength(password)
            
            print(f"\nGenerated password: {password}")
            print(f"Strength: {strength}")
            
            save = input("Save this password? (y/n): ")
            if save.lower() == 'y':
                service = get_service_name()
                username = get_username()
                add_password(service, username, password)
                display_message(f"Password saved for {service}!")
        
        elif choice == '5':
            # Delete password
            service = get_service_name()
            confirm = input(f"Delete password for {service}? (y/n): ")
            
            if confirm.lower() == 'y':
                if delete_password(service):
                    display_message(f"Password deleted for {service}")
                else:
                    display_message(f"No password found for {service}")
        
        elif choice == '6':
            display_message("Goodbye!")
            break
        
        else:
            display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()