import telebot
import calendar
import time
import gtts

bot = telebot.TeleBot('1730611798:AAHYvIqkWX5lZGwy-Hsg7DapH3BUwRCdZg4')


@bot.message_handler(content_types=['text']) 
def get_text_messages(message):
    message_splitted = message.text.lower().split('=')

    command = message_splitted[0].strip()
    text = message_splitted[1].strip()
    chat_id = message.chat.id 

    if message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'скажи =, tell = , fr =, ja =, it =, de =  ')



    elif message_splitted[0].strip() == 'скажи':
    #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'
        audio = gtts.gTTS(text, lang='ru')
        audio.save('/home/neo-d/videos/' + filename)

        bot.send_message(message.chat.id, 'ваше аудио готово щас ')
        bot.send_message(message.chat.id, 'сейчас отправлю!')

        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)
    
    elif message_splitted[0].strip() == 'tell':
        #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'
        audio = gtts.gTTS(text, lang='en')
        audio.save('/home/neo-d/videos/' + filename)

        bot.send_message(message.chat.id, 'ваше аудио готово щас ')
        bot.send_message(message.chat.id, 'сейчас отправлю!')

        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)
    elif message_splitted[0].strip() == 'fr':
        #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'
        audio = gtts.gTTS(text, lang='fr')
        audio.save('/home/neo-d/videos/' + filename)

        bot.send_message(message.chat.id, 'ваше аудио готово щас ')
        bot.send_message(message.chat.id, 'сейчас отправлю!')

        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)
    elif message_splitted[0].strip() == 'ja':
        #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'
        audio = gtts.gTTS(text, lang='ja')
        audio.save('/home/neo-d/videos/' + filename)

        bot.send_message(message.chat.id, 'ваше аудио готово щас ')
        bot.send_message(message.chat.id, 'сейчас отправлю!')

        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)
    elif message_splitted[0].strip() == 'it':
        #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'
        audio = gtts.gTTS(text, lang='it')
        audio.save('/home/neo-d/videos/' + filename)

        bot.send_message(message.chat.id, 'ваше аудио готово щас ')
        bot.send_message(message.chat.id, 'сейчас отправлю!')

        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)
    elif message_splitted[0].strip() == 'de':
        #создаем имя файла с помощью временой метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'
        audio = gtts.gTTS(text, lang='de')
        audio.save('/home/neo-d/videos/' + filename)

        bot.send_message(message.chat.id, 'ваше аудио готово щас ')
        bot.send_message(message.chat.id, 'сейчас отправлю!')

        audio_file = open('/home/neo-d/videos/' + filename, 'rb')
        bot.send_audio(message.chat.id, audio_file)



print('оки доки:')
bot.polling()