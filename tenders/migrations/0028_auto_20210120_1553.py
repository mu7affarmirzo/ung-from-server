# Generated by Django 2.2.2 on 2021-01-20 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0027_auto_20210120_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filetender',
            old_name='fileurl_en',
            new_name='en_fileurl',
        ),
        migrations.RenameField(
            model_name='filetender',
            old_name='fileurl_ru',
            new_name='ru_fileurl',
        ),
        migrations.RenameField(
            model_name='filetender',
            old_name='fileurl_uz',
            new_name='uz_fileurl',
        ),
        migrations.AlterField(
            model_name='tender',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 15, 53, 27, 932514), verbose_name='date_end'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 15, 53, 27, 932514), verbose_name='date_published'),
        ),
    ]
