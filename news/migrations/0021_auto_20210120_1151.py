# Generated by Django 2.2.2 on 2021-01-20 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20210120_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 11, 51, 51, 493696), verbose_name='date_published'),
        ),
    ]
