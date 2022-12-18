from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.misc import _


main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
settings_button = KeyboardButton(_('SETTINGS'))
main_keyboard.add(settings_button)
