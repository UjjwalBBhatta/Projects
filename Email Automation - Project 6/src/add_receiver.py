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


def add_receiver_interactive():
    """
    USER INTERFACE: Handles the input prompts and calls the logic function.
    """
    print("\n--- ADD NEW RECEIVER ---")
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    
    if name and email:
        add_receiver(name, email)
    else:
        print("❌ Name and Email cannot be empty.")

# This block allows you to test this file individually if you want
if __name__ == "__main__":
    add_receiver_interactive()