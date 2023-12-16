from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from app.common.conf.path_conf import EnvPath

class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=EnvPath,
        extra='ignore',
    )

    # service
    ENVIRONMENT: Literal['prod', 'dev', 'test']
    SERVICE_PORT: int
    RELOAD: bool

    # log
    LOG_STDOUT_FILENAME: str = 'access.log'
    LOG_STDERR_FILENAME: str = 'error.log'

    # database
    PG_HOST: str
    PG_PORT: str
    PG_USER: str
    PG_PASSWORD: str
    PG_DATABASE: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

def get_setting():
    return Setting()

settings = get_setting().model_dump()
