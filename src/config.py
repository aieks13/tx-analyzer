from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    API_TOKEN: str

    I18N_DOMAIN: str = ''
    BASE_DIR: Path = Path(__file__).parent
    LOCALES_DIR: Path = BASE_DIR / 'locales'

    ADDRESSES_LIMIT_PER_USER: int = 3

    PORTFOLIO_TRACKER_LINK: str = 'https://debank.com/profile'


settings = Settings()
