# Generated by Django 2.2.2 on 2021-01-18 05:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0022_auto_20210118_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 10, 2, 32, 22069), verbose_name='date_end'),
        ),
    ]
