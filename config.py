from telebot import TeleBot
from datetime import datetime
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

DB_NAME = os.path.join(BASE_DIR, "sqlite_db.db")

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set! Перевір .env файл")

bot = TeleBot(BOT_TOKEN)

START_TIME = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

