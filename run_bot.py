import telebot
from telebot.types import LabeledPrice, ShippingOption
from KeyBoard import kb_price_usd, kb_usd_rub, kb_price_rub, kb_yes_no


token = 'your token'
provider_token = ''
bot = telebot.TeleBot(token)

# Создаем словарь, где будут раниться валюта и количество денег от каждого пользователя, аналог машины состояний
money = {}

# Стартовая функция с отправкой фото, приветствия и клавиатуры для выбора валюты
@bot.message_handler(commands=['start'])
def start_func(message):
    with open('support_us.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo, caption='Привет, я бот, который, в отличии от вас, готовится \n'
                                          'ко дню рождения вашего коллеги! Выбери валюту в которой бы '
                                          'ты хотел прислать подарок ему на такой знаменательный день!', reply_markup=kb_usd_rub)
    money[message.chat.id] = {}


# Отправка клавиатуры с русской валютой
@bot.message_handler(func=lambda message: message.text == 'RUB')
def rub_keyboard(message):
    bot.send_message(message.chat.id, 'Выбери, сколько хочешь перевести, коллега)', reply_markup=kb_price_rub)
    money[message.chat.id]['Currency'] = "rub"


# Отправка клавиатуры с долларами
@bot.message_handler(func=lambda message: message.text == 'USD')
def usd_keyboard(message):
    bot.send_message(message.chat.id, 'Выбери, сколько хочешь перевести, коллега)', reply_markup=kb_price_usd)
    money[message.chat.id]['Currency'] = "usd"


# Списки для реакции именно на эти сообщения
money_list_rub = ['50 рублей', '200 рублей', '500 рублей', '1000 рублей']
money_list_usd = ['50 долларов', '200 долларов', '500 долларов', '1000 долларов']


# Функция для подверждения пользователем суммы и вылюты
@bot.message_handler(func=lambda message: message.text in money_list_rub)
def money_func(message):
    rub = message.text.split()[0]
    money[message.chat.id]['amount'] = rub
    # bot.send_message(message.chat.id, text=f'Вы хотите прислать {rub} рублей?')
    bot.send_message(message.chat.id,
                     f'Вы хотите отправить деньги в валюте {money[message.chat.id]["Currency"]}'
                     f' в количестве {money[message.chat.id]["amount"]}?', reply_markup=kb_yes_no)


# Функция для подверждения пользователем суммы и вылюты
@bot.message_handler(func=lambda message: message.text in money_list_usd)
def money_func(message):
    usd = message.text.split()[0]
    money[message.chat.id]['amount'] = usd
    bot.send_message(message.chat.id, f'Вы хотите отправить деньги в валюте {money[message.chat.id]["Currency"]}'
                                      f'в количестве {money[message.chat.id]["amount"]}?', reply_markup=kb_yes_no)



# Реакция на кнопки "Нет" и "Сменить валюту"
@bot.message_handler(func=lambda message: message.text == 'Нет' or message.text == 'Сменить валюту')
def back_to_start(message):
    bot.send_message(message.chat.id, 'Хорошо, давай начнем заново, выбери валюту, '
                                      'в которой хочешь подарить деньги', reply_markup=kb_usd_rub)



# После подверждения валюты и суммы начинаем платеж
@bot.message_handler(func=lambda message: message.text == 'Да')
def money_present(message):
    if money[message.chat.id]['Currency'] == 'usd':
        bot.send_invoice(chat_id=message.chat.id,
                         title='На день рождения коллеги!',
                         description='Он будет очень рад, приходить на чай 18.05',
                         invoice_payload='ДР',
                         provider_token=provider_token,
                         currency="RUB",
                         prices=[LabeledPrice(label='День рождения', amount=int(money[message.chat.id]['amount'] + '00') * 80)],
                         is_flexible=False,
                         start_parameter='123')
    else:
        bot.send_invoice(chat_id=message.chat.id,
                         title='На день рождения коллеги!',
                         description='Он будет очень рад, приходить на чай 18.05',
                         invoice_payload='ДР',
                         provider_token=provider_token,
                         currency="RUB",
                         prices=[
                             LabeledPrice(label='День рождения', amount=int(money[message.chat.id]['amount'] + '00'))],
                         is_flexible=False,
                         start_parameter='123')



@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True, error_message='Ой ой ой')


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    if int(money[message.chat.id]['amount']) < 500:
        bot.send_message(message.chat.id, 'Урааа, спасибо тебе!')
    else:
        bot.send_message(message.chat.id, 'Урааа, SUPERспасибо тебе!')


@bot.message_handler(func=lambda message: message.text == 'Закрыть')
def close_func(message):
    bot.send_message(message.chat.id, "Зачем ты меня закрываешь? Ты что, не хочешь порадовать человека?")


@bot.message_handler()
def other_message(message):
    bot.send_message(message.chat.id, 'Мы тут вопрос денег решаем, а не переписываемся) '
                                      'Давай снова начнем с выбора валюты!', reply_markup=kb_usd_rub)


bot.infinity_polling(skip_pending=True)



