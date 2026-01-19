### Daily French Email Sender

A simple Python project that emails you **10 random French words every day**, along with their English translations. Perfect for casual daily language learning with zero effort.

---

## Features

* Randomly selects **10 French words** from a text file
* Automatically **translates French → English**
* Sends a **daily email** using Gmail
* Lightweight and easy to customize

---

## Requirements

Install the dependencies with:

```bash
pip install deep-translator google-auth google-auth-oauthlib google-api-python-client google-cloud yagmail
```

**Libraries used:**

* `deep-translator` – Google Translate wrapper
* `yagmail` – Simple Gmail SMTP client
* `random` – Word selection

---

## Project Structure

```
.
├── main.py
├── french_words.txt
└── README.md
```

* `french_words.txt` should contain **one French word per line**

---

## Setup

### 1. Gmail App Password

You must enable **2-Step Verification** on your Gmail account and generate an **App Password**.

 Google Account → Security → App passwords

### 2. Configure Credentials

**Do NOT hardcode credentials in production.**
Use environment variables instead:

```python
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_APP_PASSWORD = os.getenv("MY_APP_PASSWORD")
```

Then set them in your system:

```bash
export MY_EMAIL="your_email@gmail.com"
export MY_APP_PASSWORD="your_app_password"
```

---

## Running the Script

```bash
python main.py
```

You’ll receive an email like:

```
Bonjour: Hello
Chat: Cat
Maison: House
...
```

---

## Automating Daily Emails

To receive emails every day, schedule the script using:

* **Cron (Linux/macOS)**
* **Task Scheduler (Windows)**
* **GitHub Actions**
* **Cloud VM / Server**

---

## Security Note

Never commit:

* Email addresses
* App passwords
* `.env` files

Add them to `.gitignore`.

---

## Future Improvements

* HTML email formatting
* Difficulty levels
* Pronunciations
* Multiple languages
* Streak tracking


