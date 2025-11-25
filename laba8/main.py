import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# БІЛЬШЕ НЕМАЄ src. НА ПОЧАТКУ
from config.config import Config
from db.database import init_db
from handlers import remind
from scheduler.tasks import check_reminders


async def main():
    logging.basicConfig(level=logging.INFO)

    await init_db()

    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(remind.router)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_reminders, 'interval', minutes=1, kwargs={'bot': bot})
    scheduler.start()

    print("Бот запущений без папки src...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
