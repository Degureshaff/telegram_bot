import telebot
import pyttsx3
import calendar
import time


bot = telebot.TeleBot('1730611798:AAHYvIqkWX5lZGwy-Hsg7DapH3BUwRCdZg4')


@bot.message_handler(content_types=['text']) 
def get_text_messages(message):
    message_splitted = message.text.lower().split('=')
    command = message_splitted[0].strip()
    text = message_splitted[1].strip()
    chat_id = message.chat.id 

    if message_splitted[0].strip() == 'скажи':
        audio_engine = pyttsx3.init()
        #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'

        # преобразуем текст в аудио и отправляем в папку 
        audio_engine.save_to_file(
            text,
            '/home/neo-d/videos/' + filename)
        
        # запуск движка аудио
        audio_engine.runAndWait()
        #отправка аудио
        bot.send_message(message.chat.id, 'ваше аудио: ')
        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)







print('ready()')
bot.polling()