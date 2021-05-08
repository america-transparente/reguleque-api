from functools import lru_cache
from pydantic import BaseSettings


class Config(BaseSettings):
    app_name: str = "Reguleque API"
    db_path: str = "mongodb://mongo_user:mongo_password@mongo:27017"
    db_name: str = "entries"
    sentry_dsn: str = None

    class Config:
        env_file = ".env"


@lru_cache()
def get_config():
    return Config()
