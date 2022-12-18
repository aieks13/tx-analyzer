from aiogram import executor

from src.misc import dp
from src.handlers import user


def on_startup():
    user.setup(dispatcher=dp)


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup(),
    )
