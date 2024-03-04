import asyncio
from aiogram import Bot, Dispatcher, types
from data.coinfig import tg_bot_token_test

bot = Bot(token=tg_bot_token_test)
dp = Dispatcher()


@dp.message()
async def start_cmd(message: types.Message):
    await message.answer('start')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
