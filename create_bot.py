from base import dp
from aiogram.utils import executor
from handlers import other, send_music, search_music
async def on_startup(_):
    print("Bot has been started!")

other.register_other_handlers(dp)
send_music.register_handlers_send(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
