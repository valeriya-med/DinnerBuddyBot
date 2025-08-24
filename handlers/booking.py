from telebot import TeleBot
from utils.storage import get_user
from utils.keyboards import date_keyboard, time_keyboard, confirm_keyboard

def register_booking(bot: TeleBot):

    @bot.message_handler(func=lambda m: get_user(m.from_user.id).get("step") == "name")
    def ask_date(message):
        user_id = message.from_user.id
        get_user(user_id)["name"] = message.text
        get_user(user_id)["step"] = "date"

        bot.send_message(message.chat.id, "Оберіть дату для бронювання:", reply_markup=date_keyboard())

    @bot.callback_query_handler(func=lambda call: call.data.startswith("date_"))
    def ask_time(call):
        user_id = call.from_user.id
        get_user(user_id)["date"] = call.data.replace("date_", "")
        get_user(user_id)["step"] = "time"
        bot.answer_callback_query(call.id)

        bot.send_message(call.message.chat.id, "Тепер оберіть час:", reply_markup=time_keyboard())

    @bot.callback_query_handler(func=lambda call: call.data.startswith("time_"))
    def ask_guest_qty(call):
        user_id = call.from_user.id
        get_user(user_id)["time"] = call.data.replace("time_", "")
        get_user(user_id)["step"] = "guests_qty"
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Зазнач кількість гостей (числом)")

    @bot.message_handler(func=lambda m: m.text.isdigit() and get_user(m.from_user.id).get("step") == "guests_qty")
    def summary_booking(message):
        user_id = message.from_user.id
        get_user(user_id)["guests_qty"] = int(message.text)
        get_user(user_id)["step"] = "confirm"

        user = get_user(user_id)
        summary = (
            f"Ім'я: {user['name']}\n"
            f"Дата: {user['date']}\n"
            f"Час: {user['time']}\n"
            f"Гостей: {user['guests_qty']}\n\n"
            f"Підтвердити бронювання?"
        )

        bot.send_message(message.chat.id, summary, reply_markup=confirm_keyboard())