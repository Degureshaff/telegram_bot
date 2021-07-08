import telebot
import requests
import json
import pytube
import calendar
import time

bot = telebot.TeleBot('1730611798:AAHYvIqkWX5lZGwy-Hsg7DapH3BUwRCdZg4')

@bot.message_handler(commands=['start', 'hi'])
def welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')

@bot.message_handler(content_types=['text']) 
def get_text_messages(message):

    if message.text.find('youtube.com/watch?v='):
        url = message.text
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_by_resolution('360p')
        bot.send_message(message.chat.id, 'мы качаем видео подождите...')
        filename = str(calendar.timegm(time.gmtime()))
        video.download(
            filename = filename,
            output_path = '/home/neo-d/videos'
        )
        bot.send_message(message.chat.id, 'мы скачали ваше видео вот держите')
        filepath = '/home/neo-d/videos/{filename}.{ext}'.format(
            filename = filename,
            ext = 'mp4'
        )
        downloaded_video = open(filepath, 'rb')
        bot.send_video(message.chat.id, downloaded_video)





print('бот работает.....')
bot.polling()