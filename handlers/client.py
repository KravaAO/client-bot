from aiogram import Router, F, types
import keyboard.inline_keyboard as kb
from data import database as db

router = Router()


@router.callback_query(F.data == "settings")
async def settings(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f'There u can change exchanges and coins\n in development',
        reply_markup=await kb.get_settings())


@router.callback_query(F.data == 'get_profile')
async def show_profile(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer('')
    await callback.message.edit_text(f'You can choose the exchanges \n'
                                     f'that suit you and soon it will be possible to add your own jack pairs or choose'
                                     f' ours.\nIf you have any problems or queries, you can always write to us here:'
                                     f'\nYour ID: {user_id}', reply_markup=await kb.get_profile())


@router.callback_query(F.data == 'back')
async def back_button(callback: types.CallbackQuery):
    user_full_name = callback.from_user.full_name
    await callback.answer('')
    await callback.message.edit_text(
        f'👋{user_full_name} Welcome to Arbitrage bot\n'
        f'This is a bot for finding the difference in currency prices on different exchanges.\n'
        f'⚠️Exchanges are always risks! Be attentive to every signal.',
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
    user_id = callback.from_user.id
    await callback.answer('')
    await callback.message.edit_text(f'You can choose the exchanges \n'
                                     f'that suit you and soon it will be possible to add your own jack pairs or choose'
                                     f' ours.\nIf you have any problems or queries, you can always write to us here:'
                                     f'\nYour ID: {user_id}', reply_markup=await kb.get_profile())


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
