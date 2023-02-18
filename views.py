from django.shortcuts import render
import time
import telebot
from bonum_app.bot import bot
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import settings


@csrf_exempt
def get_message(request):
    if request.method == 'POST':
        json_string = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        print(request, 'GET_MESSAGE')
        return HttpResponse('!', 200)
    return HttpResponse('Method Not Allowed', 405)

bot.set_webhook(url=f'bot.bonum.tech/{settings.BOT_TOKEN}')
