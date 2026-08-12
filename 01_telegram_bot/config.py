import os
from dotenv import load_dotenv


load_dotenv()

# TOKEN
TOKEN = os.getenv("TOKEN")

# HANDLE ERROR
if not TOKEN:
    raise ValueError("TOKEN is not set. Check your .env file.")