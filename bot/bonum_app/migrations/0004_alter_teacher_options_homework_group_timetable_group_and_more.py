# Generated by Django 4.1.3 on 2023-02-18 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0003_timebot_alter_adminbotuser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AddField(
            model_name='homework',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bonum_app.group', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bonum_app.group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='id',
            field=models.TextField(auto_created=True, primary_key=True, serialize=False, verbose_name='Номер домашнего задания'),
        ),
    ]
