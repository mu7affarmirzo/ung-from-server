# Generated by Django 2.2.2 on 2020-12-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0005_remove_tenderlot_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymodel',
            name='company_slug',
            field=models.SlugField(blank=True),
        ),
    ]
