# Generated by Django 2.2.2 on 2021-06-07 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0030_auto_20210602_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 12, 21, 33, 910067), verbose_name='date_end'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 12, 21, 33, 910067), verbose_name='date_published'),
        ),
    ]
