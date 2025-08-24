from telebot import types
from datetime import datetime, timedelta
from config import START_TIME

def date_keyboard():
    markup = types.InlineKeyboardMarkup()
    today = datetime.today()
    dates = [(today + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(7)]

    for i in range(0, len(dates), 3):
        row = [types.InlineKeyboardButton(d, callback_data=f"date_{d}") for d in dates[i:i+3]]
        markup.add(*row)
    return markup

def time_keyboard():
    markup = types.InlineKeyboardMarkup()
    times = [(START_TIME + timedelta(hours=i)).strftime("%H:%M") for i in range(24)]
    for i in range(0, len(times), 6):
        row = [types.InlineKeyboardButton(t, callback_data=f"time_{t}") for t in times[i:i+6]]
        markup.add(*row)
    return markup

def confirm_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Все вірно ✅", callback_data="confirm:yes"),
        types.InlineKeyboardButton("Скасувати ❌", callback_data="confirm:no")
    )
    return markup