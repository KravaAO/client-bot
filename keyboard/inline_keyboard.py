from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import database as db

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Settings', callback_data='settings')],
    [InlineKeyboardButton(text='Pay', callback_data='get_pay')],
    [InlineKeyboardButton(text='profile', callback_data='get_profile')]
])


async def get_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Pay', callback_data='get_pay'))
    keyboard.add(InlineKeyboardButton(text='profile', callback_data='get_profile'))
    keyboard.add(InlineKeyboardButton(text='about program', callback_data='info'))

    return keyboard.adjust(2).as_markup()


async def get_profile():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Start', callback_data='back'))
    keyboard.add(InlineKeyboardButton(text='Settings', callback_data='settings'))
    keyboard.add(InlineKeyboardButton(text='Back', callback_data='back'))

    return keyboard.adjust(2).as_markup()


async def get_settings():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='exchanges', callback_data='settings_exchanges'))
    keyboard.add(InlineKeyboardButton(text='coins', callback_data='back'))
    keyboard.add(InlineKeyboardButton(text='Back', callback_data='back_in_profile'))

    return keyboard.adjust(2).as_markup()


async def get_settings_exchanges(user_id):
    exchanges = ['okx', 'mexc', 'binance', 'huobi', 'bitget', 'bybit']
    keyboard = InlineKeyboardBuilder()
    for exchange in exchanges:
        if await db.check_exchange(user_id, exchange):
            keyboard.add(InlineKeyboardButton(text=f'✅{exchange}', callback_data=exchange))
        else:
            keyboard.add(InlineKeyboardButton(text=f'{exchange}', callback_data=exchange))
    keyboard.add(InlineKeyboardButton(text='Back', callback_data='back_in_settings'))
    return keyboard.adjust(2).as_markup()


async def pay_choice():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='25$/10d', callback_data='rate_25_10'))
    keyboard.add(InlineKeyboardButton(text='50$/30d', callback_data='rate_50_30'))
    keyboard.add(InlineKeyboardButton(text='75$/60d', callback_data='rate_75_60'))
    keyboard.add(InlineKeyboardButton(text='back', callback_data='back'))
    return keyboard.adjust(3).as_markup()


async def get_link():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Pay', callback_data='link'))

    return keyboard.adjust(1).as_markup()
