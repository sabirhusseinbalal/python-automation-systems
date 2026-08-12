from bot import TelegramBot
from config import TOKEN


def main():
    bot = TelegramBot(TOKEN)
    bot.start()


if __name__ == "__main__":
    main()