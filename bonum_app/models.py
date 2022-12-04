from django.db import models


class Teacher(models.Model):
    first_name = models.TextField()

    second_name = models.TextField()

    last_name = models.TextField()

    contact = models.TextField()

    objects = models.Manager()


class Discipline(models.Model):
    short_name = models.TextField()

    full_name = models.TextField()

    teacher = models.OneToOneField(Teacher,
                                   on_delete=models.CASCADE)

    default_room = models.TextField()

    objects = models.Manager()


class Time(models.Model):
    start = models.TextField()
    end = models.TextField()

    objects = models.Manager()


class Timetable(models.Model):
    discipline = models.OneToOneField(Discipline,
                                      on_delete=models.CASCADE)
    room = models.TextField()

    week_day = models.IntegerField(choices=((1, 'Понедельник'),
                                            (2, 'Вторник'),
                                            (3, 'Среда'),
                                            (4, 'Четверг'),
                                            (5, 'Пятница'),
                                            (6, 'Суббота')))

    week_type = models.BooleanField(choices=((True, 'Четная'),
                                             (False, 'Нечетная')))

    time = models.OneToOneField(Time,
                                on_delete=models.CASCADE)

    objects = models.Manager()


class HomeworkType(models.Model):
    name = models.TextField()

    objects = models.Manager()


class Homework(models.Model):
    id = models.TextField(primary_key=True,
                          null=False,
                          blank=False)

    exp_date = models.TextField()

    type = models.OneToOneField(HomeworkType,
                                on_delete=models.CASCADE)

    subject = models.OneToOneField(Discipline,
                                   on_delete=models.CASCADE)

    description = models.TextField()

    objects = models.Manager()


class AdminBotUser(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True)

    nickname = models.TextField(null=False,
                                blank=True)

    full_name = models.TextField(null=True,
                                 blank=True)

    objects = models.Manager()


class Group(models.Model):
    group_chat_id = models.BigIntegerField(primary_key=True)

    admins = models.ManyToManyField(to=AdminBotUser,
                                    related_name='groups')

    objects = models.Manager()
