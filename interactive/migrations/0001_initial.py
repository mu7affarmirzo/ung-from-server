# Generated by Django 2.2.2 on 2021-06-17 06:19

from django.db import migrations, models
import interactive.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(blank=True, max_length=500, null=True)),
                ('birth_date', models.CharField(blank=True, max_length=500, null=True)),
                ('topic', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=interactive.models.upload_location)),
            ],
        ),
    ]
