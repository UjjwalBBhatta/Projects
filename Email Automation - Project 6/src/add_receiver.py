import json

def add_receiver(name, email):
    """This function adds a new receiver to the receivers.json file.
    It first checks if receiver allready exists, and
    then appends this information to the JSON file.
    """
    # Load existing receivers
    try:
        with open('receivers.json', 'r') as file:
            receivers = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        receivers = {"receivers": []}
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    # Check if receiver already exists
    for receiver in receivers['receivers']:
        if receiver['email'] == email:
            print(f"Receiver with email {email} already exists.")
            return
    # Add new receiver
    new_receiver = {
        "name": name,
        "email": email
    }
    # Append and save back to file
    receivers['receivers'].append(new_receiver)
    with open('receivers.json', 'w') as file:
        json.dump(receivers, file, indent=4)
    print(f"Receiver {name} with email {email} added successfully.")

    
if __name__ == "__main__":
    print("--- Add New Email Receiver ---")
    user_name = input("Enter name: ")     # No need for str(), input is always string
    user_email = input("Enter email: ")
    
    add_receiver(user_name, user_email)