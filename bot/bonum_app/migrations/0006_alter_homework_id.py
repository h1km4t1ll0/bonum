# Generated by Django 4.1.7 on 2023-02-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonum_app', '0005_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
