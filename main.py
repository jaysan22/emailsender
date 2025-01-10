import os
import random
import base64
from deep_translator import GoogleTranslator
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request  # Fix for the error
from email.mime.text import MIMEText

# Change the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the French Words
with open("C:/Users/talkt/OneDrive - Haileybury/2025/French/french_words.txt", "r", encoding="utf-8") as file:
    french_words = [line.strip() for line in file.readlines()]

# Translate Words
def translate_words(words, target_language="en"):
    translations = []
    for word in words:
        translated_word = GoogleTranslator(source='fr', target=target_language).translate(word)
        translations.append(f"{word}: {translated_word}")
    return translations

# Gmail API Authentication Setup
def authenticate_gmail():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
    # Check if token.json exists and load credentials
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If no credentials or invalid credentials, authenticate user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(os.getcwd(), 'credentials.json'), SCOPES)  # Ensure correct path to credentials.json
            # Use a fixed port for the local server
            creds = flow.run_local_server(port=8080)
        # Save credentials for future use
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
    # Return Gmail API service
    service = build("gmail", "v1", credentials=creds)
    return service

# Create and Send Email
def send_email(service, recipient, subject, body):
    message = MIMEText(body)
    message["to"] = recipient
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
    message = {"raw": raw}

    service.users().messages().send(userId="me", body=message).execute()

# Main Function to Generate and Send Email
def daily_email():
    random_words = random.sample(french_words, 10)
    translated_words = translate_words(random_words)
    word_list = "\n".join(translated_words)

    subject = "Your Daily French Words"
    body = f"Here are your 10 French words for today:\n\n{word_list}"

    try:
        service = authenticate_gmail()
        send_email(service, "pulselitepro@gmail.com", subject, body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Run the Script
if __name__ == "__main__":
    daily_email()
