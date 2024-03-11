from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Settings', callback_data='settings')],
    [InlineKeyboardButton(text='Pay', callback_data='get_pay')],
    [InlineKeyboardButton(text='profile', callback_data='get_profile')]
])


async def get_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Pay', callback_data='get_pay'))
    keyboard.add(InlineKeyboardButton(text='profile', callback_data='get_profile'))
    keyboard.add(InlineKeyboardButton(text='Settings', callback_data='settings'))

    return keyboard.adjust(2).as_markup()


async def get_profile():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Back', callback_data='back'))

    return keyboard.adjust(1).as_markup()


async def get_settings():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='exchanges', callback_data='back'))
    keyboard.add(InlineKeyboardButton(text='coins', callback_data='back'))
    keyboard.add(InlineKeyboardButton(text='Back', callback_data='back'))

    return keyboard.adjust(2).as_markup()
