# Generated by Django 4.1.3 on 2023-01-29 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0007_alter_discipline_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='group',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='bonum_app.group', verbose_name='Группа'),
        ),
    ]