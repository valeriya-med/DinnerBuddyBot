from config import bot
from handlers import start, booking, confirm
from utils.storage import init_db

init_db()

start.register_start(bot)
booking.register_booking(bot)
confirm.register_confirm(bot)

bot.polling(none_stop=True)
