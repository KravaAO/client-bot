from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Settings', callback_data='settings')],
    [InlineKeyboardButton(text='Pay', callback_data='get_pay')],
    [InlineKeyboardButton(text='profile', callback_data='get_profile')]
])


async def get_profile():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Back', callback_data='back'))

    return keyboard.adjust(1).as_markup()
