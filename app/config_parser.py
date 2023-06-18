from typing import Optional, Union

from pydantic import BaseModel, BaseSettings, SecretStr


class TelegramConfig(BaseModel):
    api_id: Optional[int] = 2040
    api_hash: Optional[str] = "b18441a1ff607e10a989891a5462e627"
    string_session: SecretStr


class SpamConfig(BaseModel):
    timer: int = 10800
    chat_id: Union[int, str]
    message: str


class Config(BaseSettings):
    telegram: TelegramConfig
    spam: SpamConfig

    class Config:
        frozen = True
        env_file = ".env"
        env_nested_delimiter = "__"
        env_file_encoding = "utf-8"
