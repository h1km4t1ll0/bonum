from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


class AdminBotUser(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True,
                                         verbose_name='ID в телеграм',
                                         null=False,
                                         blank=False
                                         )

    nickname = models.TextField(verbose_name='Никнейм',
                                null=False,
                                blank=False)

    full_name = models.TextField(verbose_name='ФИО',
                                 null=False,
                                 blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'#{self.telegram_id} @{self.nickname}'

    class Meta:
        verbose_name = 'Админ бота'
        verbose_name_plural = 'Админы бота'


class Group(models.Model):
    group_chat_id = models.BigIntegerField(primary_key=True,
                                           verbose_name='ID чата в ТГ',
                                           null=False,
                                           blank=False
                                           )

    name = models.TextField(verbose_name='Название группы',
                            null=True,
                            blank=True
                            )

    '''имя группы, учеьное заведение, курс, факультет
    добавить ввод этих полей в боте'''
    admins = models.ManyToManyField(to=AdminBotUser,
                                    related_name='groups',
                                    verbose_name='Администраторы чата',
                                    blank=False
                                    )

    objects = models.Manager()

    def __str__(self):
        return f'#{str(self.name)}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Teacher(models.Model):
    first_name = models.TextField(verbose_name='Имя',
                                  null=False,
                                  blank=False)

    second_name = models.TextField(verbose_name='Фамилия',
                                   null=False,
                                   blank=False)

    last_name = models.TextField(verbose_name='Отчество',
                                 null=False,
                                 blank=False)

    contact = models.TextField(verbose_name='Контакты',
                               null=False,
                               blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Discipline(models.Model):
    short_name = models.TextField(verbose_name='Краткое название',
                                  null=False,
                                  blank=False)

    full_name = models.TextField(verbose_name='Полное название',
                                 null=False,
                                 blank=False)

    teacher = models.ForeignKey(Teacher,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False)

    default_room = models.TextField(verbose_name='Аудитория',
                                    null=False,
                                    blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.short_name}'

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class TimeBot(models.Model):
    name = models.TextField(verbose_name='Номер пары',
                            null=False,
                            blank=False)

    start = models.TextField(verbose_name='Начало',
                             null=False,
                             blank=False)
    end = models.TextField(verbose_name='Конец',
                           null=False,
                           blank=False)

    start1 = models.TextField(verbose_name='Начало',
                              null=False,
                              default='',
                              blank=False)
    end2 = models.TextField(verbose_name='Конец',
                            default='',
                            null=False,
                            blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Время пар'
        verbose_name_plural = 'Время пар'


class Timetable(models.Model):
    discipline = models.ForeignKey(Discipline,
                                   on_delete=models.CASCADE,
                                   verbose_name='Дисциплина',
                                   null=False,
                                   blank=False)

    room = models.TextField(verbose_name='Аудитория',
                            null=False,
                            blank=True)

    week_day = models.IntegerField(choices=((1, 'Понедельник'),
                                            (2, 'Вторник'),
                                            (3, 'Среда'),
                                            (4, 'Четверг'),
                                            (5, 'Пятница'),
                                            (6, 'Суббота')),
                                   verbose_name='День недели',
                                   null=False,
                                   blank=False
                                   )

    week_type = models.IntegerField(choices=((0, 'Четная'),
                                             (1, 'Нечетная'),
                                             (2, 'Все недели')),
                                    verbose_name='Четность недели',
                                    null=False,
                                    blank=False
                                    )

    time = models.ForeignKey(TimeBot,
                             on_delete=models.CASCADE,
                             verbose_name='Время',
                             null=False,
                             blank=False
                             )

    group = models.ForeignKey(to=Group,
                              on_delete=models.CASCADE,
                              default=None,
                              verbose_name='Группа')

    first_time_save = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.discipline.short_name} {self.time}'

    def clean(self):
        if Timetable.objects.filter(week_type=self.week_type, week_day=self.week_day, time=self.time, group=self.group):
            raise ValidationError(_('Проверьте чётность недели, в это время пара уже есть!'))  # Todo: дублкат
        if self.week_type == 2:
            if list(Timetable.objects.filter(week_type=1, week_day=self.week_day, time=self.time, group=self.group)) + \
                    list(Timetable.objects.filter(week_type=0, week_day=self.week_day, time=self.time,
                                                  group=self.group)):
                raise ValidationError(_('Проверьте чётность недели, в это время пара уже есть!'))

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class HomeworkType(models.Model):
    name = models.TextField(verbose_name='Тип домашней работы',
                            null=False,
                            blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип домашнего задания'
        verbose_name_plural = 'Типы домашнего задания'


class Homework(models.Model):
    exp_date = models.DateField(verbose_name='Дедлайн',
                                null=False,
                                blank=False
                                )

    type = models.ForeignKey(HomeworkType,
                             on_delete=models.CASCADE,
                             verbose_name='Тип домашней работы',
                             null=False,
                             blank=False
                             )

    subject = models.ForeignKey(Discipline,
                                on_delete=models.CASCADE,
                                verbose_name='Дисциплина',
                                null=False,
                                blank=False
                                )

    description = models.TextField(verbose_name='Описание',
                                   null=False,
                                   blank=False)

    group = models.ForeignKey(to=Group,
                              on_delete=models.CASCADE,
                              default=None,
                              verbose_name='Группа'
                              )

    objects = models.Manager()

    def __str__(self):
        return f'#{self.id} {self.subject.short_name}'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


@receiver(post_save, sender=Timetable)
def change_log_checked_handler(sender, instance: Timetable, *args, **kwargs):
    if not instance.first_time_save:
        instance.room = instance.discipline.default_room
        instance.first_time_save = True
        instance.save()
