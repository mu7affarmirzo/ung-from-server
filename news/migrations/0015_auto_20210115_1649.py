# Generated by Django 2.2.2 on 2021-01-15 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20210115_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingdata',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ratingdata',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ratingdata',
            name='text_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 16, 49, 20, 409312), verbose_name='date_published'),
        ),
    ]