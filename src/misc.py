from aiogram import Bot, Dispatcher

from src.config import settings
from src.middlewares.localization import i18n


bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot=bot)

_ = i18n.gettext
