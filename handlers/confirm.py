from utils.storage import get_user, delete_user, save_user

def register_confirm(bot):
    @bot.callback_query_handler(func=lambda c: c.data.startswith("confirm:"))
    def confirm_booking(call):
        user_id = call.from_user.id
        user = get_user(user_id)

        if not user or user.get("step") != "confirm":
            bot.answer_callback_query(call.id)
            return

        choice = call.data.split(":", 1)[1]
        bot.answer_callback_query(call.id)

        if choice == "yes":
            save_user(user_id)
            bot.send_message(call.message.chat.id, "Бронювання підтверджено ✅")
        else:
            delete_user(user_id)
            bot.send_message(call.message.chat.id, "Бронювання скасовано ❌")


