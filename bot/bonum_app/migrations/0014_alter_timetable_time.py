# Generated by Django 4.1.7 on 2023-02-19 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0013_timetable_first_time_save_alter_timetable_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bonum_app.timebot', verbose_name='Время'),
        ),
    ]
