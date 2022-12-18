from aiogram import Dispatcher
from aiogram.dispatcher.filters import (Command, CommandStart, CommandHelp,
                                        ChatTypeFilter, Text)

from src.misc import _
from .auth import start, set_language
from .info import info
from .settings import (settings, close_settings, inline_language_settings,
                       back_to_settings)


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
        set_language, Text(startswith='language')
    )

    # settings menu
    dispatcher.register_message_handler(
        settings, Text(_('SETTINGS')),
        state='*'
    )
    dispatcher.register_message_handler(
        settings, Command(['settings']),
        state='*'
    )

    dispatcher.register_callback_query_handler(
        close_settings, Text('close')
    )
    dispatcher.register_callback_query_handler(
        inline_language_settings, Text('set-language')
    )
    dispatcher.register_callback_query_handler(
        back_to_settings, Text('back-to-settings')
    )
