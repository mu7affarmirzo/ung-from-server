# Generated by Django 2.2.2 on 2021-07-01 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0009_auto_20210701_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 17, 23, 51, 242054), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='mailsmodel',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 17, 23, 51, 242054), verbose_name='date_subscribed'),
        ),
        migrations.AlterField(
            model_name='questionairemodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 17, 23, 51, 242054), verbose_name='date_created'),
        ),
    ]