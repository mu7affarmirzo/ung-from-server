# Generated by Django 2.2.2 on 2021-02-22 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0030_auto_20210127_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 22, 15, 20, 27, 461161), verbose_name='date_end'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 22, 15, 20, 27, 461161), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='tenderlot',
            name='price',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]