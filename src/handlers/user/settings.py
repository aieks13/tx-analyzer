from aiogram import types

from src.misc import _
from src.keyboards.inline import settings_keyboard, modified_lang_keyboard


async def settings(message: types.Message):
    await message.reply(_('SETTINGS MESSAGE'), reply=False,
                        reply_markup=settings_keyboard)
    await message.delete()


async def close_settings(callback: types.CallbackQuery):
    await callback.message.delete()


async def inline_language_settings(callback: types.CallbackQuery):
    await callback.message.edit_text(_('CHOOSE NEW LANGUAGE'),
                                     reply_markup=modified_lang_keyboard)


async def back_to_settings(callback: types.CallbackQuery):
    await callback.message.edit_text(_('SETTINGS MESSAGE'),
                                     reply_markup=settings_keyboard)
