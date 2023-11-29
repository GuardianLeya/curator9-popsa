import telebot

bot = telebot.Breabad_bot('6648365986:AAHHykLKUkczYXKD5rxP22iHUcXhV0GiDiY')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Слышь, ты, лысый', parse_mode='Markdown')


@bot.message_handler(commands=['meta-formulation'])
def main(message):
    bot.send_message(message.chat.id, 'C4H11N5')


@bot.message_handler(commands=['your plans'])
def main(message):
    bot.send_message(message.chat.id, 'Курить, жрать «Читос» и дро***')


bot.infinity_polling()