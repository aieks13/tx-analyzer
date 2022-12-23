from aiogram import Dispatcher
from aiogram.dispatcher.filters import (Command, CommandStart, CommandHelp,
                                        ChatTypeFilter, Text)

from src.misc import _
from src.states.wallets_menu import WalletsMenu, AddWalletAddress
from .auth import start, set_language
from .info import info
from .settings import (settings, close_settings, inline_language_settings,
                       back_to_settings)
from .wallets import (wallets_menu, close_wallets_menu, new_wallet, add_address,
                      close_already_exists_error, close_invalid_address_error,
                      set_label, skip_label_setting, cancel,
                      addresses_remove_menu, back_to_wallets_menu)


def setup(dispatcher: Dispatcher):
    # start and help commands
    dispatcher.register_message_handler(
        start, CommandStart(),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )
    dispatcher.register_message_handler(
        info, CommandHelp(),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )

    # language selection
    dispatcher.register_callback_query_handler(
        set_language, Text(startswith='language'),
        ChatTypeFilter(chat_type='private'),
    )

    # settings menu
    dispatcher.register_message_handler(
        settings, Text(_('SETTINGS')),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )
    dispatcher.register_message_handler(
        settings, Command(['settings']),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )

    dispatcher.register_callback_query_handler(
        close_settings, Text('close'),
        ChatTypeFilter(chat_type='private')
    )
    dispatcher.register_callback_query_handler(
        inline_language_settings, Text('set-language'),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )
    dispatcher.register_callback_query_handler(
        back_to_settings, Text('back-to-settings'),
        ChatTypeFilter(chat_type='private')
    )

    # wallets menu
    dispatcher.register_message_handler(
        wallets_menu, Text(_('MY ADDRESSES')),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )
    dispatcher.register_callback_query_handler(
        back_to_wallets_menu, Text('back-to-addresses-menu'),
        ChatTypeFilter(chat_type='private'),
        state=WalletsMenu.management
    )
    dispatcher.register_callback_query_handler(
        close_wallets_menu, Text('close'),
        ChatTypeFilter(chat_type='private'),
        state=WalletsMenu.main
    )
    dispatcher.register_callback_query_handler(
        new_wallet, Text('add-wallet-address'),
        ChatTypeFilter(chat_type='private'),
        state=WalletsMenu.main
    )
    dispatcher.register_message_handler(
        add_address,
        ChatTypeFilter(chat_type='private'),
        state=AddWalletAddress.input_address
    )
    dispatcher.register_callback_query_handler(
        close_invalid_address_error, Text('close'),
        ChatTypeFilter(chat_type='private'),
        state=AddWalletAddress.input_address
    )
    dispatcher.register_callback_query_handler(
        close_already_exists_error, Text('close'),
        ChatTypeFilter(chat_type='private'),
        state=AddWalletAddress.input_address
    )
    dispatcher.register_message_handler(
        set_label,
        ChatTypeFilter(chat_type='private'),
        state=AddWalletAddress.set_label
    )
    dispatcher.register_callback_query_handler(
        skip_label_setting, Text('skip'),
        ChatTypeFilter(chat_type='private'),
        state=AddWalletAddress.set_label
    )
    dispatcher.register_callback_query_handler(
        cancel, Text('cancel'),
        ChatTypeFilter(chat_type='private'),
        state='*'
    )
    dispatcher.register_callback_query_handler(
        addresses_remove_menu, Text('del-wallet-address'),
        ChatTypeFilter(chat_type='private'),
        state=WalletsMenu.main
    )
