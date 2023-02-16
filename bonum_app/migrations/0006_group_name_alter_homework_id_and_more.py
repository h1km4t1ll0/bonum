# Generated by Django 4.1.3 on 2023-01-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0005_alter_homework_group_alter_timetable_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='id',
            field=models.TextField(auto_created=True, primary_key=True, serialize=False, verbose_name='Номер домашнего задания'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='week_type',
            field=models.BooleanField(blank=True, choices=[(True, 'Четная'), (False, 'Нечетная'), (None, 'Все недели')], null=True, verbose_name='Четность недели'),
        ),
    ]
