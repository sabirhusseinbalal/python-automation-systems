import discord
from discord.ext import commands

from commands import (
    hello,
    echo,
    help_command,
    poll,
    calc,
    about,
    user_id
)


class DiscordBot:

    def __init__(self, token, log_channel):

        self.token = token
        self.log_channel = log_channel

        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        # Disable Discord's default !help
        self.bot = commands.Bot(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

        self.register_events()
        self.register_commands()


    #  ---------------- LOGGING  ----------------

    async def log(self, message):

        channel = discord.utils.get(
            self.bot.get_all_channels(),
            name=self.log_channel
        )

        if channel:
            await channel.send(message)


    #  ---------------- EVENTS  ----------------

    def register_events(self):

        @self.bot.event
        async def on_ready():

            message = (
                f"Bot started successfully as "
                f"{self.bot.user.name}"
            )

            print(message)

            await self.log(
                f"INFO | {message}"
            )


        @self.bot.event
        async def on_member_join(member):

            await self.log(
                f"INFO | Member joined: {member.name}"
            )

            try:
                await member.send(
                    f"Welcome to the server {member.name}!"
                )

            except discord.Forbidden:
                await self.log(
                    f"WARNING | Could not DM {member.name}"
                )


        @self.bot.event
        async def on_message(message):

            if message.author == self.bot.user:
                return

            # Simple word filter
            if "shit" in message.content.lower():

                await message.delete()

                await message.channel.send(
                    f"{message.author.mention} "
                    f"don't use that word!"
                )

                await self.log(
                    f"WARNING | Bad word detected from "
                    f"{message.author}"
                )

            await self.bot.process_commands(message)


        @self.bot.event
        async def on_command_error(ctx, error):

            await self.log(
                f"ERROR | {ctx.author} | "
                f"{type(error).__name__}: {error}"
            )



    #  ---------------- COMMANDS  ----------------

    def register_commands(self):

        # !hello
        @self.bot.command(name="hello")
        async def hello_command(ctx):

            await self.log(
                f"INFO | {ctx.author} used !hello"
            )

            await hello(ctx)


        # !echo
        @self.bot.command(name="echo")
        async def echo_command(ctx, *, message):

            await self.log(
                f"INFO | {ctx.author} used !echo"
            )

            await echo(ctx, message)


        # !help
        @self.bot.command(name="help")
        async def help_command_route(ctx):

            await self.log(
                f"INFO | {ctx.author} used !help"
            )

            await help_command(ctx)


        # !poll
        @self.bot.command(name="poll")
        async def poll_command(ctx, *, question):

            await self.log(
                f"INFO | {ctx.author} used !poll"
            )

            await poll(ctx, question)


        # !calc
        @self.bot.command(name="calc")
        async def calc_command(ctx, *, expression):

            await self.log(
                f"INFO | {ctx.author} used !calc"
            )

            await calc(ctx, expression)


        # !about
        @self.bot.command(name="about")
        async def about_command(ctx):

            await self.log(
                f"INFO | {ctx.author} used !about"
            )

            await about(ctx)


        # !id
        @self.bot.command(name="id")
        async def id_command(ctx):

            await self.log(
                f"INFO | {ctx.author} used !id"
            )

            await user_id(ctx)


    #  ---------------- START  ----------------

    def start(self):

        self.bot.run(self.token)