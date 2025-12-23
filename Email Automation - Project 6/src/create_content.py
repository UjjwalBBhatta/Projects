import json
import os

# Where we save the "Ready to Send" settings
CONFIG_FILE = 'email_config.json'
RECEIVERS_FILE = 'receivers.json'
DEFAULT_TEMPLATE = 'template.txt'

def save_email_config(subject, template_path):
    """Saves the current email settings so the Sender module can use them."""
    config = {
        "subject": subject,
        "template_path": template_path
    }
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        print("✅ Draft saved successfully!")
    except Exception as e:
        print(f"❌ Error saving config: {e}")

def preview_template(template_path):
    """Reads the template and shows a preview using the first receiver found."""
    # 1. Read the template file
    try:
        with open(template_path, 'r') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: {template_path} not found.")
        return False

    # 2. Get a dummy user from receivers.json for the preview
    try:
        with open(RECEIVERS_FILE, 'r') as f:
            data = json.load(f)
            if data['receivers']:
                sample_user = data['receivers'][0] # Take the first person
            else:
                sample_user = {"name": "Test User", "email": "test@example.com"}
    except:
        sample_user = {"name": "Test User", "email": "test@example.com"}

    # 3. RENDER THE PREVIEW
    try:
        preview_text = template_content.format(
            name=sample_user['name'], 
            email=sample_user['email']
        )
        
        print("\n" + "="*10 + " PREVIEW " + "="*10)
        print(preview_text)
        print("="*29 + "\n")
        return True
    except KeyError as e:
        print(f"❌ Template Error: You used a placeholder {e} that doesn't exist in the receiver data.")
        return False

def create_interactive():
    print("\n--- CREATE EMAIL CONTENT ---")
    
    # 1. Ask for Subject
    subject = input("Enter Email Subject: ").strip()
    if not subject:
        print("Subject cannot be empty.")
        return

    # 2. Ask for Template File
    path = input(f"Enter Template Filename (default: {DEFAULT_TEMPLATE}): ").strip()
    if not path:
        path = DEFAULT_TEMPLATE

    # 3. Show Preview
    if preview_template(path):
        # 4. Confirm and Save
        confirm = input("Does this look correct? (y/n): ").lower()
        if confirm == 'y':
            save_email_config(subject, path)
        else:
            print("❌ Draft discarded.")

if __name__ == "__main__":
    create_interactive()