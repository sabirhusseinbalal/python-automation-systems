import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
LOG_CHANNEL = "bot-logs"

if not TOKEN:
    raise ValueError("TOKEN is not set.")
