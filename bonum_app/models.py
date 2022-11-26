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


class Time(models.Model):
    start = models.TextField()
    end = models.TextField()


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


class HomeworkType(models.Model):
    name = models.TextField()


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


class Privacy(models.Model):
    telegram_admin = models.BigIntegerField(primary_key=True)

    name = models.TextField()
