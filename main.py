import asyncio
from aiogram import Bot, Dispatcher
from data.config import tg_bot_token_test
from handlers import handlers
from data import database as db


async def on_startup(_):
    await db.db_start()
    print('bd is started')


async def main():
    bot = Bot(token=tg_bot_token_test)
    dp = Dispatcher()
    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await db.db_start()
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == "__main__":
    asyncio.run(main())
    print('bot is started')
