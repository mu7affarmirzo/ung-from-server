# Generated by Django 2.2.2 on 2021-01-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20201207_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ungnewsmodel',
            name='news_title_uz',
            field=models.TextField(null=True),
        ),
    ]