import datetime
from .weather import *
import settings
from .keyboards import *
from .models import *
from .bd_scripts import *
from .status_check import check

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    if check(init_group(bot.get_chat_administrators(message.chat.id),
                        message.chat)) == 'OK':
        bot.send_message(message.chat.id,
                         'Инициализация новой группы завершена')
    else:
        bot.send_message(message.chat.id,
                         'Текущая группа уже находится в базе')


@bot.message_handler(commands=['today'])
def start_command(message):
    print(AdminBotUser.objects.all())


    current_day = datetime.datetime.now().weekday()
    weather = Weather(settings.OPEN_WEATHER_TOKEN,
                      latitude=54.84,
                      longitude=83.10)
    if check(get_homework_by_day(current_day + 1,
                                 message.chat.id)) == 'OK':
        homeworks = "\n".join(get_homework_by_day(current_day + 1,
                                                  message.chat.id))
        bot.send_message(message.chat.id,
                         f'Доброе утро! Сегодня {get_verbose_weekday(current_day + 1)}, '
                         f'{weather.compile()}\nРасписание на сегодня: \n\n{homeworks}')
    else:
        bot.send_message(message.chat.id,
                         'Произошла ошибка, обратитесь к системному админимтратору')




@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)
