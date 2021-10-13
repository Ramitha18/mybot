import os
import telebot


bot = telebot.TeleBot("2096027278:AAHWHQDxmv4G1NF8K56sn3zn0kPdDijnbCo")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hey! I'm Ramitha's bot. How can I help you?")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "Hey! How you doing?")



bot.polling()
