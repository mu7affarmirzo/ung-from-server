# Generated by Django 2.2.2 on 2020-12-22 06:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import ungfiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('ungfiles', '0003_auto_20201222_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='WithoutCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fileurl_ru', models.FileField(upload_to=ungfiles.models.upload_location)),
                ('fileurl_en', models.FileField(upload_to=ungfiles.models.upload_location)),
                ('fileurl_uz', models.FileField(upload_to=ungfiles.models.upload_location)),
                ('date_published', models.DateTimeField()),
                ('url', models.URLField(blank=True, null=True)),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='without', to='ungfiles.OffCategory')),
            ],
        ),
    ]