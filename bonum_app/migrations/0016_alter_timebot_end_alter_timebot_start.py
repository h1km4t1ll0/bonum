# Generated by Django 4.1.7 on 2023-02-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0015_alter_discipline_teacher_alter_timetable_week_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timebot',
            name='end',
            field=models.TimeField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='timebot',
            name='start',
            field=models.TimeField(verbose_name='Начало'),
        ),
    ]
