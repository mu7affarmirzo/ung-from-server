# Generated by Django 2.2.2 on 2021-06-01 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0028_auto_20210120_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 12, 3, 5, 892824), verbose_name='date_end'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 12, 3, 5, 891821), verbose_name='date_published'),
        ),
    ]