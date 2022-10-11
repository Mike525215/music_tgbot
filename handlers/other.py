from base import bot, types, Dispatcher

async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Введи автора и название песни, которую хочешь послушать')

def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=["start"])