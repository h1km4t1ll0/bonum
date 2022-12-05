import settings
from .keyboards import *
from .models import *
from .bd_scripts import *
from .status_check import check

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    """print(message.text)"""
    if check(init_group(bot.get_chat_administrators(message.chat.id),
                        message.chat)) == 'OK':
        bot.send_message(message.chat.id,
                         'Инициализация новой группы завершена')
    else:
        bot.send_message(message.chat.id,
                         'Текущая группа уже находится в базе')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)
