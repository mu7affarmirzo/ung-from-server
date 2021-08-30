# Generated by Django 2.2.2 on 2021-08-25 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_languagesmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraeducationinfomodel',
            options={'verbose_name': 'Qo‘shimcha ma’lumot (malaka oshirish, kurslar, boshqalar)', 'verbose_name_plural': 'Qo‘shimcha ma’lumot (malaka oshirish, kurslar, boshqalar)'},
        ),
        migrations.AlterModelOptions(
            name='languagesmodel',
            options={'verbose_name': 'Xorijiy tillarni bilish', 'verbose_name_plural': 'Xorijiy tillarni bilish'},
        ),
        migrations.CreateModel(
            name='SkillsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=500, null=True)),
                ('level', models.CharField(blank=True, max_length=500, null=True)),
                ('upploadcv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.UploadCv')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.CharField(blank=True, max_length=500, null=True)),
                ('date_ended', models.CharField(blank=True, max_length=500, null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('achievements', models.CharField(blank=True, max_length=500, null=True)),
                ('reason', models.CharField(blank=True, max_length=500, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=500, null=True)),
                ('upploadcv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.UploadCv')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalInformationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.CharField(blank=True, max_length=500, null=True)),
                ('salary', models.CharField(blank=True, max_length=500, null=True)),
                ('driver_licence', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=500, null=True)),
                ('confirmation', models.CharField(blank=True, max_length=500, null=True)),
                ('how_did_you_find', models.CharField(blank=True, max_length=500, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=500, null=True)),
                ('upploadcv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.UploadCv')),
            ],
        ),
    ]
