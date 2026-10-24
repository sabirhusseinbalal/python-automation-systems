import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

if not EMAIL or not PASSWORD:
    raise ValueError(
        "EMAIL or EMAIL_PASSWORD is missing. Check your .env file."
    )