# :)
import telebot

token = 'Your token here'
bot = telebot.TeleBot(token=token, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def echo(message):
    bot.send_message(message.chat.id, "Hello, User")


bot.polling()

# created by kharezmi
