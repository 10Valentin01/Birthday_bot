import telebot
from telebot.types import LabeledPrice, ShippingOption
from KeyBoard import kb_price

token = '5899670736:AAHSOd4tCcD05niucPNo9-m4pTWJ-tx9zzM'
provider_token = '381764678:TEST:59087'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_func(message):
    with open('support_us.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo, caption='Привет, я бот, который, в отличии от вас, готовится \n'
                                          'ко дню рождения вашего коллеги! Выбери сумму, которую бы '
                                          'ты хотел прислать ему на такой знаменательный день!', reply_markup=kb_price)

bot.infinity_polling(skip_pending = True)



