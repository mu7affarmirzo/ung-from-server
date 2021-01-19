# Generated by Django 2.2.2 on 2021-01-08 06:38

from django.db import migrations, models
import tenders.models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0018_auto_20210108_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetender',
            name='fileurl_en',
            field=models.FileField(blank=True, null=True, upload_to=tenders.models.location_fo_upload),
        ),
        migrations.AlterField(
            model_name='filetender',
            name='fileurl_ru',
            field=models.FileField(blank=True, null=True, upload_to=tenders.models.location_fo_upload),
        ),
        migrations.AlterField(
            model_name='filetender',
            name='fileurl_uz',
            field=models.FileField(blank=True, null=True, upload_to=tenders.models.location_fo_upload),
        ),
    ]