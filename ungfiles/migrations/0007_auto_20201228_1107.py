# Generated by Django 2.2.2 on 2020-12-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ungfiles', '0006_auto_20201222_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='filename',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='documents',
            name='filename_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='filename_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='filename_uz',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
