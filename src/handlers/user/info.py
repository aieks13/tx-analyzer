from aiogram import types

from src.misc import _


async def info(message: types.Message):
    await message.reply(_('INFO MESSAGE'), reply=False)
    await message.delete()
