import telebot
import requests
import json
import pytube
import calendar
import time

bot = telebot.TeleBot('1897153800:AAG6W-C8swxBCt9R_eoBaYQOcOpYWqGVQu8')

weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=fa0c69065a227aae0ae1081d5953bcfa&units=metric'

covid_url = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'

@bot.message_handler(commands=['start', 'hi'])
def welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')

@bot.message_handler(content_types=['text']) 
def get_text_messages(message):

    if message.text == 'привет':
        bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, '/help погода, /help cord, /help hello, /help video')
    elif message.text.lower() == '/help погода':
        bot.send_message(message.chat.id,'если хочешь узнать погоду пример: погода ru moscow')
    elif message.text.lower() == '/help cord':
        bot.send_message(message.chat.id,'если хочешь узнать кординаты пример: cord ru moscow')
    elif message.text.lower() == '/help hello':
        bot.send_message(message.chat.id,'напиши привет!')
    elif message.text.lower() == '/help video':
        bot.send_message(message.chat.id,' вставте ссылку видео из youtube!')
    elif message.text.lower() == 'спасибо':
        bot.send_animation(message.chat.id,'https://media.giphy.com/media/zzALYeLqMLDa6PEV2C/giphy.gif')
    elif message.text.split(' ')[0] == 'погода':
        textsplitted = message.text.lower().split(' ')
        city = textsplitted[2]
        country = textsplitted[1]
        w_final_url = weather_url.format(city=city, country=country)
        response = requests.get(w_final_url)
        pog_json  = response.json()
        country = pog_json['sys']['country']
        gor = pog_json['name']
        temp = pog_json['main']['temp']
        feel = pog_json['main']['feels_like']
        wind = pog_json['wind']['speed']
        bot.send_message(message.chat.id,f'код страны { country }')
        bot.send_message(message.chat.id,f'погода в городе { gor }')
        bot.send_message(message.chat.id,f'{ temp } градусов')
        bot.send_message(message.chat.id,f'ошушается как { feel }')
        bot.send_message(message.chat.id,f'скорость ветра { wind } км/ч')
    
    elif message.text.split(' ')[0] == 'cord':
        textsplitted = message.text.lower().split(' ')
        city = textsplitted[2]
        country = textsplitted[1]
        w_final_url = weather_url.format(city=city, country=country)
        response = requests.get(w_final_url)
        cord_json  = response.json()
        lat = cord_json['coord']['lat'] 
        lon = cord_json['coord']['lon'] 
        bot.send_message(message.chat.id,f' широта : { lat }')
        bot.send_message(message.chat.id,f'долгота : { lon }')
    
    elif message.text.split(' ')[0].lower() == 'covid':
        text = message.text.split(' ')
        country_code = text[1]
        wcovid_url = covid_url.format( country = country_code )
        res = requests.get(wcovid_url)
        re_json  = res.json()

        con = re_json['All']['confirmed']
        de = re_json['All']['deaths']
        re = re_json['All']['recovered']
        co = re_json['All']['country']
        po = re_json['All']['population']

        bot.send_message(message.chat.id, f'🤒 { con }')
        bot.send_message(message.chat.id, f'💀 { de }')
        bot.send_message(message.chat.id, f'😷 { re }')
        bot.send_message(message.chat.id, f'страна :{ co }')
        bot.send_message(message.chat.id,f'Население : { po }')






    else:
        bot.send_message(message.chat.id, 'я не понимаю что это значит напишите /help')







print('бот работает.....')
bot.polling()