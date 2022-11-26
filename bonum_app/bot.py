import telebot
import settings
from .models import *

bot = telebot.TeleBot(settings.BOT_TOKEN)


def get_teacher():
    Teacher.objects.get(first_name='Ivan')  # загетить запись
    Teacher.objects.all()
    Teacher.objects.filter(first_name='Ivan')  # вернет список согласно фильтру

    Teacher(first_name='vmmdfv').save()

    teacher = Teacher.objects.get(first_name='Ivan')
    teacher.delete()

    disp = Discipline.objects.get(short_name='Math')
    disp_teacher_name = disp.teacher.first_name
