import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
LOG_CHANNEL = "bot-logs"

if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set.")