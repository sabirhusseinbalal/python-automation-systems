# Discord Bot with Python

## Description

A simple Discord bot built with Python. It responds to commands, creates polls, performs calculations, and welcomes new members.

This is the second project in my **Automation Systems & Bots** group. I built it to practice working with APIs, async programming, and Discord events.

---

## What this project does

- Responds to Discord commands
- Echoes messages and performs calculations
- Creates polls with 👍 and 👎 reactions
- Shows user information
- Welcomes new members through DM
- Filters a specific bad word
- Logs bot activity and errors in a Discord channel

---

## Available Commands

| Command | Purpose |
|---|---|
| `!hello` | Show a greeting |
| `!echo hello` | Repeat a message |
| `!help` | Show available commands |
| `!poll Do you like Python?` | Create a poll |
| `!calc 10 + 5` | Perform a calculation |
| `!about` | Show bot information |
| `!id` | Show Discord user information |

---

## Modules Used

- `discord.py` – Connects Python to Discord
- `python-dotenv` – Loads the bot token from `.env`
- `operator` – Performs basic calculations

---

## Project Structure

```text
02_discord_bot/
├── main.py
├── bot.py
├── commands.py
├── config.py
├── .env
└── requirements.txt
```

---

## How to Run

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file and add your Discord bot token:

   ```env
   TOKEN=your_bot_token
   ```

3. Enable **Message Content Intent** and **Server Members Intent** in the Discord Developer Portal.

4. Make sure the bot has the required permissions and add a text channel named `bot-logs` to your server.

5. Run the bot:

   ```bash
   python main.py
   ```

**Note:** This project is for learning purposes. The calculator supports basic operations using two numbers, and the bad-word filter checks for one specific word.
