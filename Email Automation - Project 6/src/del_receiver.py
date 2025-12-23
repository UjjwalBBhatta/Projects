import json

def del_receiver(email):
    """This function deletes a receiver from the receivers.json file.
    It first checks if the receiver exists, and
    then removes this information from the JSON file.
    """
    # Load existing receivers
    try:
        with open('receivers.json', 'r') as file:
            receivers = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No receivers found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    # Check if receiver exists and remove
    for receiver in receivers['receivers']:
        if receiver['email'] == email:
            receivers['receivers'].remove(receiver)
            with open('receivers.json', 'w') as file:
                json.dump(receivers, file, indent=4)
            print(f"Receiver with email {email} deleted successfully.")
            return
    print(f"No receiver found with email {email}.")

def del_receiver_interactive():
    """Wrapper to ask for input before calling the logic function"""
    print("\n--- DELETE RECEIVER ---")
    email = input("Enter email to delete: ").strip()
    if email:
        del_receiver(email)

if __name__ == "__main__":
    del_receiver_interactive()