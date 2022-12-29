# En Birinchi telegram botimizga kerek bolgan modullerdi shaqirip alamiz

from aiogram import *
from config import TOKEN
from pytube import YouTube

# Botimizga BotFatherden algan tokendi beremiz
# proxy_url = 'http://proxy.server:3128'
# bot = Bot(token=TOKEN, proxy=proxy_url)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


# start Buyrigin jaratamiz

@dp.message_handler(commands={"start"})
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Sotcial Media Audio Jukllewshi botina xush kelipsiz\nSiz bul jerge Youtube tag'i\nqalegen videonin linkin taslasaniz linktagi\nvideoni men mp3 formatta jibere alaman ")



# Egerde messege_handlerde commanda berilmegen bolsa paydalaniwshidan kelgen xabarlardi oz ishine aladi.

@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    try:
        from io import BytesIO
        buffer = BytesIO()
        yt = YouTube(url)
    except:
        await bot.send_message(chat_id, "Qosiq Tabilmadi")
    else:
        try:
            await bot.send_message(chat_id, f"Qosiq Tartilmaqta...")
            audio = yt.streams.get_audio_only()
            audio.stream_to_buffer(buffer=buffer)
            buffer.seek(0)
            filename = f"{yt.title}"
            Caption = f"Kanal Ati: {yt.author}\n" \
                      f"Kanalga Qosiliw: {yt.channel_url}"
            await message.answer_audio(audio=buffer, caption=Caption, title=filename)
        except:
            await bot.send_message(chat_id, "Qosiq Tabilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
