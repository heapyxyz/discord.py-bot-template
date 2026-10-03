from dotenv import load_dotenv
import os

from .bot import *


def main():
    load_dotenv()
    token = os.environ.get("BOT_TOKEN")

    if not token:
        raise Exception("BOT_TOKEN variable isn't set")

    bot = Bot()
    bot.run(token)
