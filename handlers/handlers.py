from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboard.inline_keyboard as kb
from data import database as db

router = Router()
user_full_name = ''


@router.message(CommandStart())
async def cmd_start(message: Message):
    global user_full_name, user_id
    await db.cmd_start_db(message.from_user.id)
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    await message.answer(
        f'Hello {user_full_name}, i`m client assistant ',
        reply_markup=await kb.get_main_keyboard())
    return user_full_name


@router.message(Command('help'))
async def get_help(message: Message):
    help_text = '/start - for start the bot\n' \
                '/help - for get help with command\n'
    await message.answer(help_text)


@router.callback_query(F.data == "settings")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer('You selected settings')
    await callback.message.edit_text(
        f'Their u can change exchanges and coins\n in development',
        reply_markup=await kb.get_settings())


@router.callback_query(F.data == 'get_profile')
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer('You selected profile')
    await callback.message.edit_text((f'there will be ur profile from our bd\n '
                                      f'in development\n'
                                      f'{str(db.show_data_profile(user_id))}'), reply_markup=await kb.get_profile())


@router.callback_query(F.data == 'get_pay')
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer('You selected get_pay', show_alert=True)
    await callback.message.answer('Succeed get_pay')


@router.callback_query(F.data == 'back')
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f'Hello {user_full_name},  i`m client assistant ',
        reply_markup=await kb.get_main_keyboard())


@router.callback_query(F.data == "settings_exchanges")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f'Their u can change exchanges\n in development',
        reply_markup=await kb.get_settings_exchanges())
