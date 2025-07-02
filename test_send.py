import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)


async def send():
    await bot.send_message(chat_id=419705898, text="✅ Test simplu: funcționează?")


if __name__ == "__main__":
    asyncio.run(send())
