import asyncio
from aiogram import Bot, Dispatcher, types, F
from data.coinfig import tg_bot_token_test
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token=tg_bot_token_test)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}, i`m client assistant ')


@dp.message(Command('help'))
async def cmd_test1(message: types.Message):
    help_text = '/start - for start the bot\n' \
                '/help - for get help with command\n'
    await message.reply(help_text)


@dp.message(Command("test"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Test button",
        callback_data="random_value")
    )
    await message.answer(
        'First test button',
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == "test")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer('Succeed test')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
