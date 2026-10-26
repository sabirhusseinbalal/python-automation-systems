# Telegram Bot with Commands

## Description

A simple Telegram bot built with Python. It can respond to commands, echo messages, perform basic calculations, and show user information.

This is the first project in my **Automation Systems & Bots** group. I built it to practice working with APIs, classes, and logging.

---

## What this project does

- Responds to Telegram commands
- Echoes messages and performs calculations
- Shows user information and current date and time
- Handles unknown commands
- Saves bot activity in a log file
- Loads the bot token from a `.env` file

---

## Available Commands

| Command | Purpose |
|---|---|
| `/start` | Start the bot |
| `/help` | Show available commands |
| `/echo hello` | Repeat a message |
| `/calc 10 + 5` | Calculate an expression |
| `/about` | Show bot information |
| `/id` | Show Telegram user information |
| `/time` | Show current date and time |

---

## Modules Used

- `pyTelegramBotAPI` – Connects Python to Telegram
- `python-dotenv` – Loads the bot token from `.env`
- `logging` – Records bot activity
- `datetime` – Gets the current date and time

---

## Project Structure

```text
01_telegram_bot/
├── main.py
├── bot.py
├── commands.py
├── config.py
├── logger.py
├── requirements.txt
├── .env
├── logs/
│   └── bot.log
└── README.md
```

---

## How to Run

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file and add your Telegram bot token:

   ```env
   TOKEN=your_bot_token
   ```

3. Run the bot:

   ```bash
   python main.py
   ```

**Note:** The calculator uses Python's `eval()`, which is unsafe for a public bot. It should be replaced with a safer method before public use.
