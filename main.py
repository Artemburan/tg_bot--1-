import os
import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv

from app.routers.start import start_router
from app.routers.animals import anims_router
from app.routers.reviews import review_router


load_dotenv()

root_router = Router()
root_router.include_routers(start_router, anims_router, review_router)


def main():
    TOKEN = os.getenv("TOKEN")

    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(root_router)
    return dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())