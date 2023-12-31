import asyncio
import logging
import schedule

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types

import config
from handlers import router


async def send_daily_message(bot, msg: types.Message):
    message_content = "Привет! Расскажи, как прошел сегодня твой день?"
    await bot.send_message(100563858, message_content)


def _send_daily_message(bot, msg: types.Message):
    print("running...")
    asyncio.create_task(send_daily_message(bot, msg))


async def main():
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    asyncio.create_task(
        dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    )

    schedule.every().day.at("20:00").do(_send_daily_message, bot, types.Message)

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
