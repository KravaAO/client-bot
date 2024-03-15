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
        f'👋{user_full_name} Welcome to Arbitrage bot\n'
        f'This is a bot for finding the difference in currency prices on different exchanges.\n'
        f'⚠️Exchanges are always risks! Be attentive to every signal.',
        reply_markup=await kb.get_main_keyboard())
    return user_full_name


@router.message(Command('help'))
async def get_help(message: Message):
    help_text = '/start - for start the bot\n' \
                '/help - for get help with command\n'
    await message.answer(help_text)


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
        await callback.message.edit_text(f'💰You have chosen the $25 tariff for 10 days!\n'
                                         f'‼️The payment link is available within 30 minutes.',
                                         reply_markup=await kb.get_link())
    elif rate_data == '50':
        await callback.message.edit_text(f'💰You have chosen the $50 tariff for 30 days!\n'
                                         f'‼️The payment link is available within 30 minutes.',
                                         reply_markup=await kb.get_link())
    elif rate_data == '75':
        await callback.message.edit_text(f'💰You have chosen the $75 tariff for 60 days!\n'
                                         f'‼️The payment link is available within 30 minutes.',
                                         reply_markup=await kb.get_link())


@router.callback_query(F.data == 'link')
async def pay_link(callback: types.CallbackQuery):
    await callback.answer('*link*', show_alert=True)


@router.callback_query(F.data == "info")
async def back_in_profile(callback: types.CallbackQuery):
    await callback.answer('Link for guide', show_alert=True)

