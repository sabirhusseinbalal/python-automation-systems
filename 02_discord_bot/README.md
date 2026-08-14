# Discord Bot with Python

## Description

A simple Discord bot built with Python and the Discord API.

This is the second project in the **Automation Systems & Bots** group. The main goal is to understand how a Python program can connect to Discord, receive commands and events, and respond automatically.

The project also introduces asynchronous programming with `async` and `await`, command handling, configuration, logging, and basic error handling.

---

## What this project does

* Responds to Discord commands
* Greets users
* Echoes messages
* Performs basic calculations
* Creates simple polls
* Shows user information
* Welcomes new members
* Filters a simple bad word
* Logs bot activity in a Discord channel
* Handles unknown commands
* Keeps the bot token outside the source code using environment variables

---

## Available Commands

| Command | Purpose |
| ---------------------- | -------------------------------- |
| `!hello` | Show a welcome message |
| `!echo <message>` | Echo a message |
| `!help` | Show available commands |
| `!poll <question>` | Create a simple poll |
| `!calc <expression>` | Perform a basic calculation |
| `!about` | Show information about the bot |
| `!id` | Show Discord user information |

Unknown commands are recorded as errors in the `#bot-logs` channel.

---

## How It Works

The basic flow of the bot is:

```text
Discord User
      ↓
Discord API
      ↓
Discord.py
      ↓
Command / Event
      ↓
Bot Handler
      ↓
Command Function
      ↓
Response to User
```

For example, when a user sends:

```text
/hello
```

Discord receives the message and Discord.py identifies the hello command.

The command route in bot.py then calls the hello() function from commands.py.

The bot finally sends a response back to Discord.

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
* `async` and `await`

### Discord Bot Development

* Discord API basics
* Bot tokens
* Command handling
* Event handling
* Message handling
* Sending messages
* Reactions
* Discord permissions
* `discord.py`
* Event-driven programming

### Configuration

* Environment variables
* `.env` files
* Keeping secrets outside source code
* Configuration validation

### Logging

* INFO logs
* WARNING logs
* ERROR logs
* Discord log channel
* Command activity logging
* Error logging

---

## Project Structure

```text
02_discord_bot/
│
├── main.py
├── config.py
├── bot.py
├── commands.py
├── .env
└── README.md
```

### File Responsibilities

**`main.py`**

Starts the application and creates the `DiscordBot` object.

**`config.py`**

Loads the Discord bot token and other configuration from environment variables.

**`bot.py`**

Contains the `DiscordBot` class and connects Discord events and commands to their corresponding functions.

**`commands.py`**

Contains the actual command functions such as `hello()`, `echo()`, `calc()`, and `poll()`.

`.env`

Stores the Discord bot token outside the source code.

---

## Logging

The bot sends important activity to the Discord `#bot-logs` channel.

Example:

```text
INFO | Bot started successfully as Idiot Bot

INFO | sabirhusseinbalal used !hello

INFO | sabirhusseinbalal used !echo

INFO | sabirhusseinbalal used !calc

WARNING | Bad word detected from sabirhusseinbalal

INFO | Member joined: it4achii_

ERROR | it4achii_ | CommandNotFound:
Command "hero" is not found
```

This allows the bot activity and errors to be monitored directly from Discord.

---

## Testing

The bot was manually tested using the main commands and events.

### Tested

* `!hello`
* `!echo`
* `!help`
* `!poll`
* `!calc`
* `!about`
* `!id`
* New member event
* Bad word filter
* Unknown commands
* Discord log channel

### Example

```text
!hello
→ Hello!

I am a Discord bot made with Python for learning.
```

```text
!echo hello sabir
→ hello sabir
```

```text
/echo
→ Usage: /echo <message>
```

```text
!calc 10 + 5
→ Result: 15.0
```

```text
!poll Do you like Python?
→ Creates a poll with 👍 and 👎 reactions
```

Unknown commands are recorded in the `#bot-logs` channel.

---

## Learning Outcome

The main purpose of this project was not to create a large Discord bot.

The goal was to understand how a Python application can communicate with Discord and respond to both commands and events.

Through this project, I learned how to:

* Connect Python to Discord
* Handle Discord commands
* Handle Discord events
* Separate command logic into modules
* Use classes and objects
* Use constructors and methods
* Understand self
* Understand basic async and await
* Manage configuration with environment variables
* Build basic Discord logging
* Handle errors
* Understand event-driven programming

This project became my first practical introduction to asynchronous programming and event handling in Python.

---

## Future Improvements

Possible improvements for a later version:

* Add more useful commands
* Improve the calculator
* Add more Discord events
* Add better permission handling
* Add automated tests
* Add database support
* Deploy the bot so it can run continuously
