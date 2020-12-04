from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField

def upload_location(instance, filename):
    file_path = 'tender/files/{title}-{filename}'.format(
        title=str(instance.title), filename=filename
    )
    return file_path


class Tender(models.Model):
    company = models.ForeignKey('CompanyModel', related_name='company_tenders', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    asosiy_talablar = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)

    status = models.BooleanField("Is Open", default=True)

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext

    def __str__(self):
        return self.title

    @property
    def tenderlots(self):
        return self.tenderlot_set.all()

class TenderLot(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class CompanyModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    inn = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    clientBillNumber = models.CharField(max_length=50, null=True, blank=True)
    deliveryTerms = models.CharField(max_length=50, null=True, blank=True)
    deadline = models.CharField(max_length=50, null=True, blank=True)
    paymentTerms = models.CharField(max_length=50, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_ends = models.DateTimeField(auto_now=True, verbose_name="date_ending")
    # company_slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name