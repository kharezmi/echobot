# :)
import telebot

token = '1883977736:AAGa-tdgjteGU3_32Rsu-w1VLu6AghmXynA'
bot = telebot.TeleBot(token=token, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def echo(message):
    bot.send_message(message.chat.id, "Hello, User")


bot.polling()