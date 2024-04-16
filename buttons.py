from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    [
        [
            
             KeyboardButton(text="Katalog"),
             KeyboardButton(text="Karzinka"),
             KeyboardButton(text="help"),  
        ]     
    ],
    resize_keyboard=True
)


admin = ReplyKeyboardMarkup(
    [
        [
             KeyboardButton(text="tavar qoshish"),
             KeyboardButton(text="tavar o'chirish"),
        ]  ,
        [
            KeyboardButton(text="Katalog qoshish"),
            KeyboardButton(text="Katalog o'chirish"),  
        ]   
    ],
    resize_keyboard=True
)