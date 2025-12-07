def get_menu_choice():
    """Get user menu choice"""
    return input("\nEnter your choice: ").strip()

def get_service_name():
    """Get service name from user"""
    return input("Enter service name (e.g., Gmail, Netflix): ").strip()

def get_username():
    """Get username from user"""
    return input("Enter username/email: ").strip()

def get_password():
    """Get password from user"""
    return input("Enter password: ").strip()

def get_master_password():
    """Get master password"""
    import getpass
    return getpass.getpass("Enter master password: ")