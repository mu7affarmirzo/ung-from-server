# Generated by Django 2.2.2 on 2021-01-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0019_auto_20210108_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='deadline',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deadline_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deadline_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deadline_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deliveryTerms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deliveryTerms_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deliveryTerms_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='deliveryTerms_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='paymentTerms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='paymentTerms_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='paymentTerms_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='paymentTerms_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]