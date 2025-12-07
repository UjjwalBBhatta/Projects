def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("PASSWORD MANAGER")
    print("="*50)
    print("1. Add new password")
    print("2. Retrieve password")
    print("3. List all services")
    print("4. Generate random password")
    print("5. Delete password")
    print("6. Exit")
    print("="*50)

def display_password(service, username, password, strength):
    """Display retrieved password"""
    print(f"\n--- {service} ---")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Strength: {strength}")

def display_services(services):
    """Display list of services"""
    print("\nStored services:")
    for i, service in enumerate(services, 1):
        print(f"{i}. {service}")

def display_message(message):
    """Display a message"""
    print(f"\n{message}")