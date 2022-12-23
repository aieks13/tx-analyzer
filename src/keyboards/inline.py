from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.misc import _


close_button = InlineKeyboardButton(_('CLOSE'), callback_data='close')
cancel_button = InlineKeyboardButton(_('CANCEL'), callback_data='cancel')
skip_button = InlineKeyboardButton(_('SKIP'), callback_data='skip')

skip_keyboard = InlineKeyboardMarkup(row_width=1)
skip_keyboard.add(skip_button)

cancel_keyboard = InlineKeyboardMarkup(row_width=1)
cancel_keyboard.add(cancel_button)

close_keyboard = InlineKeyboardMarkup(row_width=1)
close_keyboard.add(close_button)


language_keyboard = InlineKeyboardMarkup(row_width=3)
en_lang_button = InlineKeyboardButton('🇬🇧 EN', callback_data='language-en')
ru_lang_button = InlineKeyboardButton('🇷🇺 RU', callback_data='language-ru')
uk_lang_button = InlineKeyboardButton('🇺🇦 UK', callback_data='language-uk')
language_keyboard.add(en_lang_button, ru_lang_button, uk_lang_button)


settings_keyboard = InlineKeyboardMarkup(row_width=2)
set_lang_button = InlineKeyboardButton(_('LANGUAGE'),
                                       callback_data='set-language')
settings_keyboard.add(set_lang_button, close_button)


modified_lang_keyboard = InlineKeyboardMarkup(row_width=3)
back_to_settings_button = InlineKeyboardButton(_('BACK'),
                                               callback_data='back-to-settings')
modified_lang_keyboard.add(en_lang_button, ru_lang_button,
                           uk_lang_button, back_to_settings_button)


wallets_menu_keyboard = InlineKeyboardMarkup(row_width=2)
add_address_button = InlineKeyboardButton(_('ADD WALLET'),
                                          callback_data='add-wallet-address')
del_address_button = InlineKeyboardButton(_('DELETE WALLET'),
                                          callback_data='del-wallet-address')
wallets_menu_keyboard.add(add_address_button, del_address_button, close_button)


modified_wallet_menu_keyboard = InlineKeyboardMarkup(row_width=1)
back_to_addresses_menu_button = InlineKeyboardButton(
    _('BACK'), callback_data='back-to-addresses-menu'
)
modified_wallet_menu_keyboard.add(back_to_addresses_menu_button)
