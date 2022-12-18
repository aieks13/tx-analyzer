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


settings = Settings()
