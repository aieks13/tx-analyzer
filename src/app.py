from aiogram import executor

from src.misc import dp
from src.middlewares.localization import i18n
from src.handlers import user


def on_startup():
    user.setup(dispatcher=dp)
    dp.middleware.setup(middleware=i18n)


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup(),
    )
