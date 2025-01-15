import random
from deep_translator import GoogleTranslator
import yagmail

# Gmail credentials (replace with your email and app password)
MY_EMAIL = "pulselitepro@gmail.com"
MY_APP_PASSWORD = "vvqk wngq galv boxz"

# Load the French Words
with open("french_words.txt", "r", encoding="utf-8") as file:
    french_words = [line.strip() for line in file.readlines()]

# Translate Words
def translate_words(words, target_language="en"):
    translations = []
    for word in words:
        translated_word = GoogleTranslator(source="fr", target=target_language).translate(word)
        translations.append(f"{word}: {translated_word}")
    return translations

# Main Function to Generate and Send Email
def daily_email():
    # Select 10 random words and translate them
    random_words = random.sample(french_words, 10)
    translated_words = translate_words(random_words)
    word_list = "\n".join(translated_words)

    # Email subject and body
    subject = "Your Daily French Words"
    body = f"Here are your 10 French words for today:\n\n{word_list}"

    try:
        # Initialize yagmail with direct credentials
        yag = yagmail.SMTP(MY_EMAIL, MY_APP_PASSWORD)
        yag.send(
            to="pulselitepro@gmail.com",
            subject=subject,
            contents=body,
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Run the Script
if __name__ == "__main__":
    daily_email()
