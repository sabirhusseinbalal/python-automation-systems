from datetime import datetime

# /start
def start(bot, message):
    bot.reply_to(
        message,
        """
Welcome to SabirLabBot!

This bot is a Python learning project.
Use /help to see available commands.
"""
    )

# /echo
def echo(bot, message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        bot.reply_to(
            message,
            "Usage: /echo <message>"
        )
        return

    text = parts[1]

    bot.reply_to(
        message,
        text
    )

# /help
def help(bot, message):
    bot.reply_to(
        message,
        """
Available commands:

/start - Start the bot
/echo  - Echo your message
/help  - Show all commands
/calc  - Calculator
/about - About this bot
/id    - Show your Telegram ID
/time  - Show current time
"""
    )

# /calc
def calc(bot, message):
    try:
        parts = message.text.split(maxsplit=1)

        if len(parts) < 2:
            raise ValueError("No calculation provided.")

        expression = parts[1]
        result = eval(expression)

        bot.reply_to(
            message,
            f"Result: {result}"
        )

    except ZeroDivisionError:
        bot.reply_to(
            message,
            "You cannot divide by zero."
        )

    except (SyntaxError, NameError, TypeError, ValueError):
        bot.reply_to(
            message,
            "Invalid calculation.\nExample: /calc 10 + 5"
        )

    except Exception:
        bot.reply_to(
            message,
            "Something went wrong while calculating."
        )

# /about
def about(bot, message):
    bot.reply_to(
        message,
        """
SabirLabBot

A Python Telegram bot built as part of
the Automation Systems & Bots learning project.

Built to learn:
• APIs
• OOP
• Command handling
• Configuration
• Logging
• Event-driven programming

Repo:
https://github.com/sabirhusseinbalal/python-automation-systems
"""
    )

# /id
def user_id(bot, message):
    user = message.from_user

    bot.reply_to(
        message,
        f"""
ID: {user.id}
First Name: {user.first_name}
Last Name: {user.last_name}
Username: {user.username}
"""
    )

# /time
def current_time(bot, message):
    current = datetime.now()

    bot.reply_to(
        message,
        f"""
----------------
Time: {current.strftime("%H:%M:%S")}
Date: {current.strftime("%d %B %Y")}
Day:  {current.strftime("%A")}
----------------
"""
    )

# Unknown message
def custom_message(bot, message):
    bot.reply_to(
        message,
        "Sorry, I don't understand that command. Use /help."
    )

