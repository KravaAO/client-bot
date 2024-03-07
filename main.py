import asyncio
from aiogram import Bot, Dispatcher
from data.config import tg_bot_token_test
from handlers import handlers


async def main():
    bot = Bot(token=tg_bot_token_test)
    dp = Dispatcher()

    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
