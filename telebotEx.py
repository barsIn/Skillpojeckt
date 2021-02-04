import telebot
from extensions import MyBotException, Converter
from config import TOKEN


bot = telebot.TeleBot(TOKEN)





@bot.message_handler(commands=['start'])
def greeteengs(message: telebot.types.Message):
    text = "Что бы начать работу, введите запрос боту в следующем формате:" \
           "\n<Имя валюты> <в какую валюту перевести> <Колличество переводимой валюты>" \
           "\n Что бы узнать курс валюты к рублю, напиши слово курс и название валюты из списка"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def no_felp(message: telebot.types.Message):
    bot.reply_to(message,
                 f"Список команд: \n/values - Возвращает список доступных валют, \n/rate - возвращает текущий курс валют, \n/start")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    currencys = Converter.getcurrency()
    currency = []
    for cur in currencys:
        currency.append(cur.getfullName())
    text = "Доступные валюты:"
    for key in currency:
        text = '\n'.join((text, key,))

    bot.reply_to(message, text)


@bot.message_handler(commands=['rate'])
def rate(message: telebot.types.Message):
    curensis = Converter.getcurrency()
    text = "Курсы валют:"
    for key in curensis:
        text = '\n'.join((text, f'{key.fullName} \n{key.price} за {key.volume}'))

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def fistfunc(message: telebot.types.Message):
    u = message.text.lower()
    if u == 'бот хороший' or u == 'хороший бот':
        bot.reply_to(message, f"Спасибо, {message.from_user.first_name}, я старался")

    else:
        mes = message.text.lower()
        mp = list(mes.split(' '))
        if mp[0].lower() == 'курс':
            mes = Converter.getcourse(mes[5:])
            bot.reply_to(message, f"{mes}")
        else:
            text = Converter.convert(mp)
            bot.reply_to(message, f"{text}")




bot.polling(none_stop=True)
