# Generated by Django 2.2.2 on 2021-01-15 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20210114_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ungnewsmodel',
            options={'verbose_name': 'pizza'},
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 16, 32, 20, 429076), verbose_name='date_published'),
        ),
    ]
