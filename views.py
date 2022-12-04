from django.shortcuts import render
import time
from bonum_app.bot import bot


def run(request):
    try:
        bot.polling(none_stop=True, interval=5)
    except Exception as e:
        time.sleep(1)
        run(request)


