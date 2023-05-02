from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime
import picture_color_handler as pch
import random
import string

API_TOKEN = '5894674597:AAEWrBJ26L_rFffyF_tTN-P46QreusR6aig'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
colors_number = 3


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Здарова!\n"
                        "Я могу обработать твою фотографию...\n"
                        "Отправь мне картинку и получи результат.\n"
                        "Отправь число, чтобы изменить количество цветов на следующей картинке.\n"
                        "Количество цветов по умолчанию: 3")


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    global colors_number
    await message.photo[-1].download(destination_file="D:/photo/bot_photos/111.jpg")
    img = pch.handle_picture("D:/photo/bot_photos/111.jpg", colors_number)
    # img = pch.get_gamma("D:/photo/bot_photos/111.jpg", colors_number)
    img.save("D:/photo/bot_photos/111.png")
    photo = types.InputFile("D:/photo/bot_photos/111.png")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    global colors_number
    if message.text.lower().find("привет") > -1:
        await message.answer("Сам ты привет")
    # elif message.text == "exit":
    #     exit()
    elif message.text.isdigit():
        number = int(message.text)
        if 1 < number < 30:
            colors_number = number
            await message.answer("Установлено количество цветов: " + str(colors_number))
    else:
        await message.answer("Все говорят \"" + message.text + "\", а ты купи слона...")
        await message.answer("Московское время " + str(datetime.strftime(datetime.now(), "%H:%M")))


if __name__ == '__main__':
    executor.start_polling(dp)
