# Generated by Django 2.2.2 on 2020-12-22 09:27

from django.db import migrations, models
import ungfiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('ungfiles', '0005_auto_20201222_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='fileurl_en',
            field=models.FileField(blank=True, null=True, upload_to=ungfiles.models.upload_location),
        ),
        migrations.AlterField(
            model_name='documents',
            name='fileurl_ru',
            field=models.FileField(blank=True, null=True, upload_to=ungfiles.models.upload_location),
        ),
        migrations.AlterField(
            model_name='documents',
            name='fileurl_uz',
            field=models.FileField(blank=True, null=True, upload_to=ungfiles.models.upload_location),
        ),
    ]
