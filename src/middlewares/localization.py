from typing import Any, Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from src.config import settings
from src.services.database import db


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> Any:
        user = types.User.get_current()
        if await db.get_user_language(user.id):
            return await db.get_user_language(user.id)
        else:
            return user.locale


i18n = Localization(domain=settings.I18N_DOMAIN, path=settings.LOCALES_DIR)
