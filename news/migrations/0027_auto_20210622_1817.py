# Generated by Django 2.2.2 on 2021-06-22 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0026_auto_20210617_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 18, 17, 32, 691644), verbose_name='date_published'),
        ),
    ]
