# Generated by Django 4.1.3 on 2023-01-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0010_remove_timetable_group_timetable_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='group',
        ),
        migrations.AddField(
            model_name='timetable',
            name='group',
            field=models.ManyToManyField(default=None, to='bonum_app.group', verbose_name='Группа'),
        ),
    ]