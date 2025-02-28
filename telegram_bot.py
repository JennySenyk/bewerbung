import telebot
import webbrowser

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://pitbullmusic.com/')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'J-Lo, {message.from_user.first_name}!')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help/b <em><u>information</u></em>')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'Hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, '/start')

bot.polling(non_stop=True)

