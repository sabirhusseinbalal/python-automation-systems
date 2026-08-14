import operator


# ---------------- Calculator ----------------

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(expression):

    parts = expression.split()

    if len(parts) != 3:
        raise ValueError("Invalid calculation.")

    left, symbol, right = parts

    left = float(left)
    right = float(right)

    if symbol not in OPERATORS:
        raise ValueError("Operation not allowed.")

    return OPERATORS[symbol](left, right)



# ---------------- Commands ----------------

# !hello
async def hello(ctx):

    await ctx.send(
        """
Hello!

I am a Discord bot made with Python for learning.
Hope you're doing well.

Use !help to see available commands.
"""
    )


# !echo
async def echo(ctx, message):

    await ctx.send(message)


# !help
async def help_command(ctx):

    await ctx.send(
        """
Available commands:

!hello - Greeting
!echo <message> - Echo your message
!help - Show available commands
!poll <question> - Create a poll
!calc <expression> - Calculator
!about - About this bot
!id - Show your Discord information
"""
    )


# !poll
async def poll(ctx, question):

    message = await ctx.send(
        f"**Poll:** {question}\n\n"
        "👍 Yes\n"
        "👎 No"
    )

    await message.add_reaction("👍")
    await message.add_reaction("👎")


# !calc
async def calc(ctx, expression):

    try:

        result = calculate(expression)

        await ctx.send(f"Result: {result}")

    except ZeroDivisionError:

        await ctx.send("You cannot divide by zero.")

    except (ValueError, TypeError):

        await ctx.send(
            "Invalid calculation.\n"
            "Example: !calc 10 + 5"
        )


# !about
async def about(ctx):

    await ctx.send(
        """
Idiot Bot

A Python Discord bot built as part of
the Automation Systems & Bots learning project.

Built to learn:

• APIs
• OOP
• Async programming
• Command handling
• Event handling
• Configuration
• Logging
"""
    )


# !id
async def user_id(ctx):

    user = ctx.author

    await ctx.send(
        f"""
User Information

ID: {user.id}
Name: {user.name}
Display Name: {user.display_name}
"""
    )