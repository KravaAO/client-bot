from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboard.inline_keyboard as kb
from data import database as db

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await db.cmd_start_db(message.from_user.id)
    user_full_name = message.from_user.full_name
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
async def settings(callback: types.CallbackQuery):
    await callback.answer('You selected settings')
    await callback.message.edit_text(
        f'There u can change exchanges and coins\n in development',
        reply_markup=await kb.get_settings())


@router.callback_query(F.data == 'get_profile')
async def show_profile(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer('You selected profile')
    await callback.message.edit_text(f'Your ID: {user_id}', reply_markup=await kb.get_profile())


@router.callback_query(F.data == 'get_pay')
async def get_pay(callback: types.CallbackQuery):
    user_full_name = callback.from_user.full_name
    await callback.answer('')
    await callback.message.edit_text(f'{user_full_name}💎Select the number of days you want to buy?',
                                     reply_markup=await kb.pay_choice())


@router.callback_query(F.data.startswith('rate_'))
async def rate(callback: types.CallbackQuery):
    rate_data = callback.data.split('_')[1]
    if rate_data == '25':
        await callback.message.answer(f'💰You have chosen the $25 tariff for 10 days!\n'
                                      f'‼️The payment link is available within 30 minutes.',
                                      reply_markup=await kb.get_link())
    elif rate_data == '50':
        await callback.message.answer(f'💰You have chosen the $50 tariff for 30 days!\n'
                                      f'‼️The payment link is available within 30 minutes.',
                                      reply_markup=await kb.get_link())
    elif rate_data == '75':
        await callback.message.answer(f'💰You have chosen the $75 tariff for 60 days!\n'
                                      f'‼️The payment link is available within 30 minutes.',
                                      reply_markup=await kb.get_link())


@router.callback_query(F.data == 'link')
async def pay_link(callback: types.CallbackQuery):
    await callback.answer('*link*', show_alert=True)


@router.callback_query(F.data == 'back')
async def back_button(callback: types.CallbackQuery):
    user_full_name = callback.from_user.full_name
    await callback.answer('')
    await callback.message.edit_text(
        f'Hello {user_full_name},  i`m client assistant ',
        reply_markup=await kb.get_main_keyboard())


@router.callback_query(F.data == "settings_exchanges")
async def settings_exchanges(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer('')
    await callback.message.edit_text(
        f'Choose the exchanges from which you want to receive signals',
        reply_markup=await kb.get_settings_exchanges(user_id))


@router.callback_query(F.data == "back_in_profile")
async def back_in_profile(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f'Their u can change exchanges\n in development',
        reply_markup=await kb.get_profile())


@router.callback_query(F.data == "back_in_settings")
async def back_in_profile(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f'Their u can change exchanges\n in development',
        reply_markup=await kb.get_settings())


@router.callback_query(F.data == "info")
async def back_in_profile(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.reply(f'This is a bot for finding the difference in currency prices on different exchanges.'
                                 f'\n Exchanges are always risks! be attentive to every signal')


@router.callback_query()
async def choice_exchanges(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    choice = callback.data
    await db.add_exchanges(user_id, choice)
    new_keyboard_markup = await kb.get_settings_exchanges(user_id)
    await callback.message.edit_text(
        f'Choose the exchanges from which you want to receive signals',
        reply_markup=new_keyboard_markup
    )

