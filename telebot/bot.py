import telebot
bot = telebot.TeleBot('1730611798:AAHoOI_rTRGrhwYMz-eYSaLzh7d2OVFWuiI')

@bot.message_handler(commands=['start', 'hi'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "Привет":
        bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши привет")
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'хорошо')
    elif message.text.lower() == 'создатель':
        bot.send_message(message.chat.id, '@apex_emir')
    elif message.text.lower() == 'python':
        bot.send_message(message.chat.id, 'Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.')
    elif message.text.lower() == 'audio':
        bot.send_audio(message.chat.id, 'https://muzon-music.com/public/vk.play.php?id=371745462_456493882&vk_hash=764_64a8d8c94dffc2962a&hash=40026f7efb4b1b400bee92c8183becbe&a=AC/DC&t=Thunderstruck&name=ac-dc_thunderstruck')
    elif message.text.lower() == 'фото':
        bot.send_photo(message.chat.id, 'https://www.google.com/imgres?imgurl=https%3A%2F%2Favatanplus.ru%2Ffiles%2Fresources%2Foriginal%2F5c5e490148135168d04d2d0f.png&imgrefurl=https%3A%2F%2Favatanplus.com%2Fdetail%2Fresource-3856280&tbnid=vT6Yy6dLXGzf0M&vet=12ahUKEwjtlK762LzxAhVCzyoKHdRxCMkQMyglegUIARCdAg..i&docid=OV0rx842PxbiuM&w=550&h=541&q=png%20%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&client=ubuntu&ved=2ahUKEwjtlK762LzxAhVCzyoKHdRxCMkQMyglegUIARCdAg')
    elif message.text.lower() == 'аман':
        bot.send_photo(message.chat.id, 'https://n1s1.hsmedia.ru/70/03/37/700337f23cd273503d1df498e073f644/500x361_0xac120003_13762508961615799384.jpg')
    elif message.text.lower() == 'стикер':
        bot.send_sticker(message.chat.id, 'https://tlgrm.ru/_/stickers/73a/aed/73aaedd6-70a6-40f1-ae0d-1c0ed846a5b3/1.webp')
    elif message.text.lower() == 'gif':
        bot.send_animation(message.chat.id, 'https://giphy.com/gifs/angrybirds-angry-birds-leonard-movie-l41Ys1fQky5raqvMQ')
    else:
        bot.send_message(message.chat.id, 'Не понимаю, что это значит.')

    


bot.polling()