# Generated by Django 2.2.2 on 2021-06-28 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0028_auto_20210628_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 28, 11, 20, 8, 629392), verbose_name='date_published'),
        ),
    ]