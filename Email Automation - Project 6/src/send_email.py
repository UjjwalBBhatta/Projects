import smtplib
import ssl
import json
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# FILES
CONFIG_FILE = 'email_config.json'
RECEIVERS_FILE = 'receivers.json'

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def send_bulk_emails_interactive():
    print("\n--- 🚀 BULK EMAIL SENDER ---")

    # 1. LOAD CONFIGURATION
    config = load_json(CONFIG_FILE)
    if not config:
        print(f"❌ Error: {CONFIG_FILE} is missing. Please create content first (Option 3).")
        return

    receivers_data = load_json(RECEIVERS_FILE)
    if not receivers_data or not receivers_data['receivers']:
        print(f"❌ Error: {RECEIVERS_FILE} is missing or empty.")
        return

    # 2. READ TEMPLATE
    template_path = config['template_path']
    try:
        with open(template_path, 'r') as f:
            template_body = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Template file '{template_path}' not found!")
        return

    # 3. GET CREDENTIALS
    print("To send these emails, we need your Gmail credentials.")
    sender_email = input("Your Gmail: ").strip()
    # Note: For production, use environment variables. For this CLI, input is fine.
    password = input("Your App Password: ").strip()

    # 4. CONFIRMATION
    count = len(receivers_data['receivers'])
    print(f"\nReady to send '{config['subject']}' to {count} people.")
    confirm = input("Type 'SEND' to confirm: ")
    
    if confirm != 'SEND':
        print("❌ Aborted.")
        return

    # 5. CONNECT & SEND
    print("\nConnecting to Gmail Server...")
    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            print("✅ Login Successful! Starting sending...")
            
            success_count = 0
            
            for person in receivers_data['receivers']:
                try:
                    # Create the email object
                    msg = MIMEMultipart()
                    msg["From"] = sender_email
                    msg["To"] = person['email']
                    msg["Subject"] = config['subject']

                    # PERSONALIZATION MAGIC
                    # If you fixed the template logic, ensure your keys match here!
                    # Example: Hello {name}!
                    personalized_body = template_body.format(
                        name=person['name']
                        # Add other keys here if your JSON has them, e.g., company=person['company']
                    )
                    
                    msg.attach(MIMEText(personalized_body, "plain"))

                    # SEND
                    server.send_message(msg)
                    print(f"   -> Sent to {person['email']}")
                    success_count += 1
                    
                    # Polite delay so Google doesn't think you are a spam bot
                    time.sleep(1) 
                    
                except Exception as e:
                    print(f"   ❌ Failed to send to {person['email']}: {e}")

            print(f"\n🎉 DONE! Successfully sent {success_count}/{count} emails.")

    except smtplib.SMTPAuthenticationError:
        print("❌ Auth Error: Check your email and App Password.")
    except Exception as e:
        print(f"❌ Fatal Error: {e}")

if __name__ == "__main__":
    send_bulk_emails_interactive()