# Generated by Django 2.2.2 on 2021-01-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0020_auto_20210114_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='address_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='address_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='address_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
