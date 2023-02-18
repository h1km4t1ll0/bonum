import datetime

import telebot.types
from .models import *
from .statuses import *


def init_group(admin_list: list[telebot.types.ChatMember],
               group_chat: telebot.types.Chat) -> Status | str:
    """
    New group initialization
    """
    try:
        if Group.objects.filter(group_chat_id=int(group_chat.id)):
            return 'model exists'

        group = Group(group_chat_id=int(group_chat.id))
        group.save()

        for admin in admin_list:
            AdminBotUser(telegram_id=int(admin.user.id),
                         nickname=admin.user.username,
                         full_name=f'{admin.user.first_name} {admin.user.last_name}').save()
            group.admins.add(AdminBotUser.objects.get(telegram_id=int(admin.user.id)))

        group.save()
        return SuccessStatus()

    except Exception as e:
        return ExceptionStatus(e)


def get_homework_by_day(day_num: int,
                        group_id: str) -> list[str] | Status:
    try:
        lessons = Timetable.objects.filter(group=Group.objects.get(group_chat_id=group_id),
                                           week_day=day_num)
        li = []
        for lesson in lessons:
            homeworks = Homework.objects.filter(exp_date=datetime.datetime.now().strftime("%d.%m.%y"),
                                                subject=lesson.discipline)

            if len(homeworks) == 0:
                li.append(f'{lesson.time.start} - {lesson.time.end} | '
                          f'{lesson.discipline.full_name} домашки нет, каб {lesson.room} '
                          f'{lesson.discipline.teacher.first_name} {lesson.discipline.teacher.last_name}')
            else:
                li.append(f'{lesson.time.start} - {lesson.time.end} | '
                          f'{lesson.discipline.full_name} домашка есть ({homeworks[0].type}), каб {lesson.room} '
                          f'{lesson.discipline.teacher.first_name} {lesson.discipline.teacher.last_name}')

        return li
        '''10:00 -11.20 | Матан  каб. 2031 домашка есть (письменно), Елена Владимировна'''
    except Exception as e:
        return ExceptionStatus(e)


def get_verbose_weekday(day_num: int) -> Status | str:
    if day_num == 0:
        return 'понедельник'
    if day_num == 1:
        return 'вторник'
    if day_num == 2:
        return 'среда'
    if day_num == 3:
        return 'четверг'
    if day_num == 4:
        return 'пятница'
    if day_num == 5:
        return 'суббота'
    if day_num == 6:
        return 'воскресенье'
    return ExceptionStatus('Error')


def check_existence(model: models.Model,
                    instance: models.Model) -> Existence:
    if len(model.objects.filter(id=instance.id)):
        return Exists()
    return NotExists()
