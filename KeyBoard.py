from telebot.types import KeyboardButton, ReplyKeyboardMarkup

kb_price_rub = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn_50_rub = KeyboardButton('50 рублей')
btn_200_rub = KeyboardButton('200 рублей')
btn_500_rub = KeyboardButton('500 рублей')
btn_1000_rub = KeyboardButton('1000 рублей')
btn_close = KeyboardButton('Закрыть')
btn_change = KeyboardButton('Сменить валюту')
kb_price_rub.add(btn_50_rub, btn_200_rub, btn_500_rub, btn_1000_rub, btn_change).add(btn_close)

kb_usd_rub = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
btn_usd = KeyboardButton('USD')
btn_rub = KeyboardButton('RUB')
kb_usd_rub.add(btn_rub, btn_usd)

kb_price_usd = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn_50 = KeyboardButton('50 долларов')
btn_200 = KeyboardButton('200 долларов')
btn_500 = KeyboardButton('500 долларов')
btn_1000 = KeyboardButton('1000 долларов')
btn_close = KeyboardButton('Закрыть')
btn_change = KeyboardButton('Сменить валюту')
kb_price_usd.add(btn_50, btn_200, btn_500, btn_1000, btn_change).add(btn_close)

kb_yes_no = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn_yes = KeyboardButton('Да')
btn_no = KeyboardButton('Нет')
kb_yes_no.add(btn_yes, btn_no)