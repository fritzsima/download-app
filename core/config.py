import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    STATIC_HOST: str = ""
    STATIC_DIR: str = './static/'
    BASE_URL: str = f'http://{APP_HOST}:{APP_PORT}'


class DevelopmentConfig(Config):
    STATIC_DIR = os.getenv('STATIC_DIR', './static/')


class LocalConfig(Config):
    APP_HOST: str = "localhost"


class ProductionConfig(Config):
    ENV: str = "production"
    DEBUG: str = False
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = os.getenv("APP_PORT", 80)
    STATIC_DIR = os.getenv("STATIC_DIR", './static/')
    BASE_URL: str = f'https://{APP_HOST}'


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
