# Generated by Django 2.2.2 on 2021-01-20 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20210115_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 9, 38, 58, 940896), verbose_name='date_published'),
        ),
    ]
