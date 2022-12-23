from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ParseMode

from src.misc import bot, _
from src.config import settings
from src.services.onchain import is_valid_address
from src.services.database import db
from src.states.wallets_menu import WalletsMenu, AddWalletAddress
from src.keyboards.inline import (wallets_menu_keyboard, cancel_keyboard,
                                  close_keyboard, skip_keyboard,
                                  modified_wallet_menu_keyboard)


async def wallets_menu(message: types.Message):
    output = ''
    if await db.count_user_addresses(message.from_user.id):
        raw_data = await db.get_address_list(message.from_user.id)
        counter = 0

        for wallet in raw_data:
            counter += 1
            label = wallet[2]
            address = wallet[1]
            output += f'{counter}. ' \
                      f'{label} ' \
                      f'<a href="{settings.PORTFOLIO_TRACKER_LINK}/{address}">'\
                      f'{address[:5]}...{address[-5:]}' \
                      f'</a>\n'

    msg = 'Remember that you can view your wallet statistics simply by using ' \
          'the /stats command, you do not need to add the address to your ' \
          'list for this\n\n' + output

    await WalletsMenu.main.set()
    await message.delete()
    await message.reply(
        _(msg), reply=False, reply_markup=wallets_menu_keyboard,
        parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


async def close_wallets_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.finish()


async def new_wallet(callback: types.CallbackQuery, state: FSMContext):
    limit = settings.ADDRESSES_LIMIT_PER_USER
    if await db.count_user_addresses(callback.from_user.id) < limit:
        await callback.message.edit_text(
            _('ADD NEW ADDRESS:'), reply_markup=cancel_keyboard
        )
        await state.update_data(first_message_id=callback.message.message_id)
        await AddWalletAddress.input_address.set()
    else:
        await callback.answer(
            _('LIMIT OF ADDRESSES REACHED (3)'), show_alert=True
        )


async def add_address(message: types.Message, state: FSMContext):
    if await is_valid_address(str(message.text)):
        if await db.is_pair_exists(message.from_user.id, message.text):
            await message.reply(
                _('THIS ADDRESS IS ALREADY ON YOUR ADDRESSES LIST'),
                reply_markup=close_keyboard
            )
        else:
            await db.add_wallet_address(message.from_user.id, message.text)
            await state.update_data(address=message.text)
            msg = await message.reply(
                _('SET LABEL FOR ADDRESS OR PRESS SKIP BUTTON'),
                reply_markup=skip_keyboard
            )
            await state.update_data(second_message_id=msg.message_id)
            data = await state.get_data()
            first_message_id = data.get('first_message_id')
            await bot.delete_message(message.from_user.id, first_message_id)
            await AddWalletAddress.set_label.set()
    else:
        await message.reply(
            _('INCORRECT ADDRESS, TRY ANOTHER ONE'),
            reply_markup=close_keyboard
        )


async def close_already_exists_error(callback: types.CallbackQuery,
                                     state: FSMContext):
    await callback.message.delete()
    await state.finish()


async def close_invalid_address_error(callback: types.CallbackQuery,
                                      state: FSMContext):
    await callback.message.delete()
    await state.finish()


async def set_label(message: types.Message, state: FSMContext):
    data = await state.get_data()
    address = data.get('address')
    await db.set_address_label(message.from_user.id, address, message.text)
    await message.reply(
        _('YOU HAVE JUST SET A LABEL [{}] FOR THE ADDRESS\n{}')
        .format(message.text, address), reply=False
    )
    second_message_id = data.get('second_message_id')
    await bot.delete_message(message.from_user.id, second_message_id)


async def skip_label_setting(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    address = data.get('address')
    await callback.message.reply(
        _('LABEL SETTING JUST SKIPPED, ADDRESS {address}SUCCESSFULLY ADDED!')
        .format(address), reply=False
    )
    second_message_id = data.get('second_message_id')
    await bot.delete_message(callback.from_user.id, second_message_id)


async def addresses_remove_menu(callback: types.CallbackQuery):
    output = ''
    if await db.count_user_addresses(callback.from_user.id):
        raw_data = await db.get_address_list(callback.from_user.id)
        counter = 0

        for wallet in raw_data:
            counter += 1
            label = wallet[2]
            address = wallet[1]
            output += f'{counter}. ' \
                      f'{label} ' \
                      f'<a href="{settings.PORTFOLIO_TRACKER_LINK}/{address}">'\
                      f'{address[:5]}...{address[-5:]}' \
                      f'</a> ❌\n'

    msg = 'Here you can remove your addresses from the list:\n\n' + output

    await WalletsMenu.management.set()
    await callback.message.edit_text(
        _(msg), reply_markup=modified_wallet_menu_keyboard,
        parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


async def back_to_wallets_menu(callback: types.CallbackQuery):
    output = ''
    if await db.count_user_addresses(callback.from_user.id):
        raw_data = await db.get_address_list(callback.from_user.id)
        counter = 0

        for wallet in raw_data:
            counter += 1
            label = wallet[2]
            address = wallet[1]
            output += f'{counter}. ' \
                      f'{label} ' \
                      f'<a href="{settings.PORTFOLIO_TRACKER_LINK}/{address}">'\
                      f'{address[:5]}...{address[-5:]}' \
                      f'</a>\n'

    msg = 'Remember that you can view your wallet statistics simply by using ' \
          'the /stats command, you do not need to add the address to your ' \
          'list for this\n\n' + output

    await WalletsMenu.main.set()
    await callback.message.edit_text(
        _(msg), reply_markup=wallets_menu_keyboard, parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.finish()
