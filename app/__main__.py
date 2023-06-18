from asyncio import sleep, run

from app.telegram import Telegram
from app import Config, log


async def main() -> None:
    config = Config()
    client = Telegram.client(
        string_session=config.telegram.string_session,
        api_id=config.telegram.api_id,
        api_hash=config.telegram.api_hash,
        logger=logger,
    )
    while True:
        await client.send_message(
            chat_id=config.spam.chat_id,
            message=config.spam.message,
        )
        await sleep(config.spam.timer)


if __name__ == "__main__":
    logger = log()
    try:
        run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Program stopped by user")
