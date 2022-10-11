from base import types, bot, Dispatcher
from time import sleep
from handlers import search_music
import os

async def send_track(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Поиск музыки...')
    sleep(5)
    try:
        file_name = search_music.download_track(msg.text)
        await bot.send_message(msg.from_user.id, 'Нашёл кое-что для тебя😉')
        await bot.send_audio(msg.from_user.id, open(f"/Users/misha/Desktop/music/{file_name}.mp3", "rb"))
        os.remove(f"/Users/misha/Desktop/music/{file_name}.mp3")
    except:
        await bot.send_message(msg.from_user.id, 'Мне ничего не удалось найти по этому запросу🙁')


def register_handlers_send(dp: Dispatcher):
    dp.register_message_handler(send_track)