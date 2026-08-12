# Telegram Bot with Commands

## Description

A simple Telegram bot built with Python and the Telegram Bot API.

This is the first project in the **Automation Systems & Bots** group. The main goal is to understand how a Python program can communicate with Telegram, receive user messages, handle commands, and respond automatically.

The project also introduces a small class-based structure, configuration management, logging, environment variables, and basic error handling.

---

## What this project does

* Responds to Telegram commands
* Greets users
* Echoes user messages
* Performs basic calculations
* Shows user information
* Shows the current date and time
* Provides information about the bot
* Handles unknown commands or messages
* Records bot activity in a log file
* Logs warnings and critical errors
* Keeps the bot token outside the source code using environment variables

---

## Available Commands

| Command              | Purpose                                  |
| -------------------- | ---------------------------------------- |
| `/start`             | Start the bot and show a welcome message |
| `/echo <message>`    | Echo a message back to the user          |
| `/help`              | Show available commands                  |
| `/calc <expression>` | Perform a basic calculation              |
| `/about`             | Show information about the project       |
| `/id`                | Show the user's Telegram information     |
| `/time`              | Show the current date and time           |

Unknown messages receive a simple fallback response.

---

## How It Works

The basic flow of the bot is:

```text
Telegram User
      ↓
Telegram Bot API
      ↓
TeleBot
      ↓
Command Handler
      ↓
Command Function
      ↓
Logger
      ↓
Response to User
```

For example, when a user sends:

```text
/start
```

the bot receives the message, identifies the `/start` command, sends the message to its handler, records the activity in the log, and finally calls the `start()` command function.

---

## Concepts Learned

This project focuses on the following Python and automation concepts:

### Python

* Functions
* Classes
* Objects
* Constructors (`__init__`)
* Methods
* `self`
* Composition
* Modules and imports
* Exception handling

### Telegram Bot Development

* Telegram Bot API basics
* Bot tokens
* Command handlers
* Message handlers
* Receiving messages
* Sending replies
* Polling / event loop
* Event-driven programming

### Configuration

* Environment variables
* `.env` files
* Keeping secrets outside source code
* Configuration validation

### Logging

* `INFO`
* `WARNING`
* `ERROR`
* `CRITICAL`
* File logging
* Console logging
* Log formatting

---

## Project Structure

```text
telegram-bot/
│
├── main.py
├── config.py
├── bot.py
├── commands.py
├── logger.py
│
├── logs/
│   └── bot.log
│
├── .env
└── README.md
```

### File Responsibilities

**`main.py`**

Starts the application and creates the `TelegramBot` object.

**`config.py`**

Loads the bot token from environment variables and checks that it exists.

**`bot.py`**

Contains the `TelegramBot` class and connects Telegram commands to their corresponding functions.

**`commands.py`**

Contains the actual command functions such as `/start`, `/help`, `/calc`, and `/time`.

**`logger.py`**

Contains the `Logger` class responsible for recording bot activity to the log file and terminal.

**`logs/bot.log`**

Stores bot activity such as commands, warnings, and critical errors.

---

## Logging

The bot records important activity while it is running.

Example:

```text
2026-08-11 17:01:44 [INFO] Bot started
2026-08-11 17:01:57 [INFO] User: sabirhusseinbalal | Command: /help
2026-08-11 17:02:12 [INFO] User: sabirhusseinbalal | Command: /calc
```

Unknown messages are recorded as warnings.

Critical application failures are recorded using the `CRITICAL` log level.

Logs are written both to:

* `logs/bot.log`
* The terminal

---

## Testing

The bot was manually tested using the main commands.

### Tested

* `/start`
* `/help`
* `/echo`
* `/calc`
* `/about`
* `/id`
* `/time`
* Unknown messages

### Example

```text
/calc 10 + 5
→ Result: 15
```

```text
/echo hello sabir
→ hello sabir
```

```text
/echo
→ Usage: /echo <message>
```

```text
/calc
→ Invalid calculation.
```

The bot activity was also checked in `logs/bot.log` to confirm that commands were being recorded correctly.

---

## Important Note About `/calc`

The calculator currently uses Python's `eval()` function to evaluate expressions.

This was intentionally used as a learning exercise, but `eval()` can execute arbitrary Python code and is **not safe for a public calculator**.

A future version should replace it with a restricted mathematical expression parser.

---

## Learning Outcome

The main purpose of this project was not to create a feature-rich Telegram bot.

The goal was to understand how a small automation application is structured.

Through this project, I learned how to:

* Connect Python to a Telegram bot
* Handle user commands
* Separate command logic into modules
* Use classes and objects
* Use constructors and methods
* Understand `self`
* Use composition
* Manage configuration with environment variables
* Build a basic logging system
* Handle exceptions
* Understand event-driven programming
* Test a small automation system

This project became my first practical introduction to building a Python application with multiple connected modules rather than keeping everything inside one file.

---

## Future Improvements

Possible improvements for a later version:

* Replace `eval()` with a safe calculator
* Add more useful bot commands
* Add a games menu linking to existing web games
* Add better error reporting
* Add automated tests
* Deploy the bot so it can run continuously

These improvements are intentionally left for future projects instead of making this first bot unnecessarily complex.
