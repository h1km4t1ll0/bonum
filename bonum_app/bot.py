import settings
from .keyboards import *
from .models import *
from bd_scripts import *

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    init_group(bot.get_chat_administrators(message.chat.id), message.chat)
    bot.send_message(message.chat.id, 'Инициализация новой группы завершена')


@bot.message_handler(content_types=['text'])
def text(message):
    print()
    bot.send_message(message.chat.id, message.text)

