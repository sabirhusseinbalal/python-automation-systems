from bot import DiscordBot
from config import TOKEN, LOG_CHANNEL


def main():

    bot = DiscordBot(
        TOKEN,
        LOG_CHANNEL
    )

    bot.start()


if __name__ == "__main__":
    main()