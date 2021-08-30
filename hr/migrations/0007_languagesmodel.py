# Generated by Django 2.2.2 on 2021-08-24 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_auto_20210824_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(blank=True, max_length=500, null=True)),
                ('writing', models.IntegerField(blank=True, null=True)),
                ('reading', models.IntegerField(blank=True, null=True)),
                ('speaking', models.IntegerField(blank=True, null=True)),
                ('upploadcv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.UploadCv')),
            ],
        ),
    ]
