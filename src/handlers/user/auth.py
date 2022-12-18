from datetime import datetime

from aiogram import types

from src.keyboards.inline import language_keyboard
from src.keyboards.static import main_keyboard
from src.services.database import db
from src.misc import bot, _


async def set_bot_commands():

    COMMANDS_LIST = {
        "en": [
            types.BotCommand('start', 'start-en'),
            types.BotCommand('help', 'help-en'),
        ],
        "ru": [
            types.BotCommand('start', 'start-ru'),
            types.BotCommand('help', 'help-ru'),
        ],
        "uk": [
            types.BotCommand('start', 'start-uk'),
            types.BotCommand('help', 'help-uk'),
        ]
    }

    for language_code, command in COMMANDS_LIST.items():
        await bot.set_my_commands(commands=command, language_code=language_code)


async def start(message: types.Message):
    await set_bot_commands()
    if not await db.is_user_registered(message.from_user.id):
        await message.reply(
            _('INITIAL'), reply_markup=language_keyboard, reply=False
        )
        await db.signup(message.from_user.id, datetime.now())
    else:
        await message.reply(
            _('BASE MESSAGE'), reply=False, reply_markup=main_keyboard
        )
    await message.delete()


async def set_language(callback: types.CallbackQuery):
    if await db.is_user_registered(callback.from_user.id):
        language = str(callback.data.split('-')[1])
        await db.set_language(callback.from_user.id, language)
        await callback.message.delete()
        await bot.send_message(
            callback.from_user.id, _('BASE MESSAGE'), reply_markup=main_keyboard
        )
    else:
        await callback.answer(_('SIGN UP ERROR'), show_alert=True)
