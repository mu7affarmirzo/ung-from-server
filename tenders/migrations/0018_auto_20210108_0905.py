# Generated by Django 2.2.2 on 2021-01-08 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0017_remove_tender_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filetender',
            name='tender',
        ),
        migrations.AddField(
            model_name='tender',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_tenders', to='tenders.CompanyModel'),
            preserve_default=False,
        ),
    ]
