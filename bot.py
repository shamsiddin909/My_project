import logging
from aiogram import Bot, Dispatcher, types, executor
from buttons import *
import database
from datetime import datetime


API_TOKEN = '6542830780:AAGncQd5uUjqoswU5hVvWP1rcMEe_SbA0mQ'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer(f"Salom - {message.from_user.first_name}\nBotimizga hush kelibsiz.\nSiz bu bot orqali ozingizga kerak bolgan Telefonlarni topishingiz mumkin", reply_markup=main)
    first_name = message.from_user.username
    telegram_id = message.from_user.id
    phone_number = +987654345678
    database.register_user(telegram_id, first_name, phone_number)

@dp.message_handler(commands=['admin'])
async def admin_panel(message:types.Message):
    if message.from_user.id == 6983244704:
        await message.answer(f'{message.from_user.first_name} - siz adminsiz✅ \nKerakli bolimni tanlang', reply_markup=admin)
    else:
        await message.answer(f'{message.from_user.first_name} - siz admin emassiz❌')   
        await message.answer(f"Salom - {message.from_user.first_name}\nBotimizga hush kelibsiz.\nSiz bu bot orqali ozingizga kerak bolgan Telefonlarni topishingiz mumkin", reply_markup=main)

@dp.message_handler(content_types=['text'])
async def text_message(message:types.Message):
    if message.text == "tavar qoshish":
        if message.from_user.id == 6983244704:
            pass
        else:
            await message.answer("Kerakli bolimni tanlang", reply_markup=admin)
    elif message.text == "tavar o'chirish":
        if message.from_user.id == 6983244704:
            pass
        else:
            await message.answer("Kerakli bolimni tanlang", reply_markup=admin)
    elif message.text == "Katalog qoshish":
        if message.from_user.id == 6983244704:
            pass
        else:
            await message.answer("Kerakli bolimni tanlang", reply_markup=admin)
        
            
    elif message.text == "Katalog o'chirish":
        if message.from_user.id == 6983244704:
            pass
        else:
            await message.answer("Kerakli bolimni tanlang", reply_markup=admin)
        
            

  
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)