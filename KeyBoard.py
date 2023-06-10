from telebot.types import KeyboardButton, ReplyKeyboardMarkup

kb_price = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn_50 = KeyboardButton('50 рублей')
btn_200 = KeyboardButton('200 рублей')
btn_500 = KeyboardButton('500 рублей')
btn_1000 = KeyboardButton('1000 рублей')
btn_close = KeyboardButton('Закрыть')
kb_price.add(btn_50, btn_200, btn_500, btn_1000, btn_close)