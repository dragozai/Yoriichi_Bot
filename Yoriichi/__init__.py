import logging
import time
from telegraph import Telegraph
from Yoriichi.config import Config
from pyrogram import Client, errors
from telethon import TelegramClient


StartTime = time.time()
logging.basicConfig(level=logging.INFO)

telegraph = Telegraph()
telegraph.create_account(short_name='Ryuuzai')

API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
DB_URI = Config.DB_URI
ALLOWED_USERS = [
        895373440
    ]
LOG_CHANNEL = Config.LOG_CHANNEL

telethn = TelegramClient(None, API_ID, API_HASH)
pgram = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
