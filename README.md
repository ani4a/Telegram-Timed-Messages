# Telegram Timed Messages

Telegram Timed Messages is a python script using telethon that allows you to send a message to a group once every certain time

## Deployment and use
Settings of the bot is determined using environment variables or `.env` file
Check the `example.env` file and create your own `.env` file.
```commandline
cp example.env .env
nano .env
```
Then run the bot using `docker compose`
```commandline
docker compose up --build
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
