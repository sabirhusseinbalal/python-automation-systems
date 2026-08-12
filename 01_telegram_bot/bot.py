import telebot

from commands import (
    start,
    echo,
    help,
    calc,
    about,
    user_id,
    current_time,
    custom_message
)

from logger import Logger, LOG_FILE


class TelegramBot:

    def __init__(self, token):
        self.token = token

        self.bot = telebot.TeleBot(self.token)

        self.logger = Logger(LOG_FILE)

        self.register_handlers()

    # REGISTER COMMAND HANDLERS
    def register_handlers(self):

        @self.bot.message_handler(commands=["start"])
        def handle_start(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /start"
            )
            start(self.bot, message)

        @self.bot.message_handler(commands=["echo"])
        def handle_echo(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /echo"
            )
            echo(self.bot, message)

        @self.bot.message_handler(commands=["help"])
        def handle_help(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /help"
            )
            help(self.bot, message)

        @self.bot.message_handler(commands=["calc"])
        def handle_calc(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /calc"
            )
            calc(self.bot, message)

        @self.bot.message_handler(commands=["about"])
        def handle_about(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /about"
            )
            about(self.bot, message)

        @self.bot.message_handler(commands=["id"])
        def handle_user_id(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /id"
            )
            user_id(self.bot, message)

        @self.bot.message_handler(commands=["time"])
        def handle_current_time(message):
            self.logger.info(
                f"User: {message.from_user.username} | Command: /time"
            )
            current_time(self.bot, message)

        # UNKNOWN MESSAGE HANDLER
        @self.bot.message_handler(func=lambda message: True)
        def handle_unknown_message(message):
            self.logger.warning(
                f"User: {message.from_user.username} | "
                f"Unknown message: {message.text}"
            )
            custom_message(self.bot, message)

    # START BOT
    def start(self):
        try:
            self.logger.wait()

            self.logger.info("Bot started")

            self.bot.polling()

        except Exception as e:
            self.logger.critical(
                f"Bot stopped unexpectedly: {e}"
            )
