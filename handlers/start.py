from telebot import TeleBot
from utils.storage import init_user, get_user
from telebot import types

def register_start(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Привіт, рад тебе бачити! Напиши своє ім'я, щоб продовжити)")
        init_user(message.from_user.id)
        get_user(message.from_user.id)["step"] = "name"