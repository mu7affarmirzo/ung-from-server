# Generated by Django 2.2.2 on 2021-07-01 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0032_auto_20210701_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 17, 17, 40, 936943), verbose_name='date_published'),
        ),
    ]
