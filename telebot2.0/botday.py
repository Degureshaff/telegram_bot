import telebot
import requests
import json


bot = telebot.TeleBot('1897153800:AAG6W-C8swxBCt9R_eoBaYQOcOpYWqGVQu8')

day_url = 'https://holidays.abstractapi.com/v1/?api_key=2872cf258d92486696bc58d963af2797&country={country}&year=2021&month={month}&day={day}'

@bot.message_handler(commands=['start', 'hi'])
def welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')
    bot.reply_to(message, 'пример команды: дата us 2 12')


@bot.message_handler(content_types=['text']) 
def get_text_messages(message):

    if message.text == 'привет':
        bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
    elif message.text.split(' ')[0].lower() == 'день':
        text = message.text.split(' ')
        country = text[1]
        month_code = text[2]
        day_code = text[3]

        day_fi = day_url.format(country = country,month = month_code, day = day_code)
        response = requests.get(day_fi)
        popjson = response.json()

        n = popjson[0]['name']
        c = popjson[0]['country']
        location = popjson[0]['location']
        week = popjson[0]['week_day']
        date = popjson[0]['date']

        bot.send_message(message.chat.id,f'название праздника:{n}')
        bot.send_message(message.chat.id,f'дата {date} ')
        bot.send_message(message.chat.id,f'город:{c}')
        bot.send_message(message.chat.id,f'локация:{location}')
        bot.send_message(message.chat.id,f'день недели:{week}')
    
    else:
        bot.send_message(message.chat.id, '?')























print('бот работает.....')
bot.polling()