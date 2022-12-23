from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.config import settings
from src.middlewares.localization import i18n


bot = Bot(token=settings.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

_ = i18n.gettext
