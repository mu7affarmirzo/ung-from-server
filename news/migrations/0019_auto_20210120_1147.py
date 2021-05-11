# Generated by Django 2.2.2 on 2021-01-20 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20210120_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 11, 47, 6, 792690), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
