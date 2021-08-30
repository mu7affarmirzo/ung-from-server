# Generated by Django 2.2.2 on 2021-08-09 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0010_auto_20210701_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationform',
            options={'verbose_name': 'Murojaatlar', 'verbose_name_plural': 'Murojaatlar'},
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 17, 45, 17, 675800), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='full_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='FIO'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='number',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='mailsmodel',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 17, 45, 17, 675800), verbose_name='date_subscribed'),
        ),
        migrations.AlterField(
            model_name='questionairemodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 17, 45, 17, 675800), verbose_name='date_created'),
        ),
    ]
