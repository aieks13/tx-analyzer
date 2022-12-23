from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.misc import _


main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
settings_button = KeyboardButton(_('SETTINGS'))
wallets_button = KeyboardButton(_('MY ADDRESSES'))
main_keyboard.add(wallets_button, settings_button)
