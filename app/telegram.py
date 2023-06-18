from typing import Union

from pydantic import SecretStr
from telethon import TelegramClient
from telethon.sessions import StringSession

from app import log


class Telegram:
    def __init__(self, client: TelegramClient, logger: log) -> None:
        self.client = client
        self.logger = logger

    @classmethod
    def client(
        cls, string_session: SecretStr, api_id: int, api_hash: str, **kwargs
    ) -> "Telegram":
        return cls(
            client=TelegramClient(
                StringSession(string_session.get_secret_value()),
                api_id=api_id,
                api_hash=api_hash,
            ),
            **kwargs,
        )

    async def send_message(self, chat_id: Union[int, str], message: str) -> None:
        async with self.client:
            await self.client.send_message(
                entity=chat_id,
                message=message,
                parse_mode="html",
            )
        self.logger.warn(
            f"Message with text: '{message}' sent in chat: '{chat_id}' successfully!"
        )
