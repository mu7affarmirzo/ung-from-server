# Generated by Django 2.2.2 on 2021-08-24 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiencemodel',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='languagesmodel',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='skillsmodel',
            name='cv',
        ),
        migrations.DeleteModel(
            name='AdditionalInformationModel',
        ),
        migrations.DeleteModel(
            name='ExperienceModel',
        ),
        migrations.DeleteModel(
            name='LanguagesModel',
        ),
        migrations.DeleteModel(
            name='SkillsModel',
        ),
    ]
