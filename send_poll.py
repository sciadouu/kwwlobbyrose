import os
import random
import asyncio
from telegram import Bot

TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = int(os.getenv("TG_CHAT_ID"))

NO_OPTIONS = [
    "Per un'altra volta / No",
    "Per sta volta passo / No",
    "Skippo / No",
    "Non ci sono / No",
    "Questa la salto / No",
]

async def main():
    bot = Bot(token=TOKEN)

    await bot.send_poll(
        chat_id=CHAT_ID,
        question="🌹 Lobby Rose — mercoledì alle 21:00\nCi sei?",
        options=[
            "Partecipo / Sì",
            random.choice(NO_OPTIONS),
        ],
        is_anonymous=False,
        allows_multiple_answers=False,
    )

asyncio.run(main())