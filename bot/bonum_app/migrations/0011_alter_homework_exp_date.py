# Generated by Django 4.1.7 on 2023-02-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0010_alter_homework_exp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='exp_date',
            field=models.DateField(verbose_name='Дедлайн'),
        ),
    ]
