import os
from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from uuid import uuid4
from django.utils import timezone
from datetime import datetime 
from django.utils.timezone import now

def upload_location(instance, filename):
    file_path = 'tender/files/{title}-{filename}'.format(
        title=str(instance.title), filename=filename
    )
    return file_path

def location_fo_upload(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'tender/files/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return str(file_path)

class FileTender(models.Model):
    filename = models.CharField(max_length=150, blank=True, null=True)
    ru_fileurl = models.FileField(upload_to=location_fo_upload, null=True, blank=True)
    en_fileurl = models.FileField(upload_to=location_fo_upload, null=True, blank=True)
    uz_fileurl = models.FileField(upload_to=location_fo_upload, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    
    def extension_ru(self):
        if self.ru_fileurl:
            name, extension = os.path.splitext(self.ru_fileurl.name)
            return str(extension)
        else:
            return None
    def extension_en(self):
        if self.en_fileurl:
            name, extension = os.path.splitext(self.en_fileurl.name)
            return str(extension)
        else:
            return None
    def extension_uz(self):
        if self.uz_fileurl:
            name, extension = os.path.splitext(self.uz_fileurl.name)
            return str(extension)
        else:
            return None



    def fileurl_ru(self):
        if self.ru_fileurl:
            url = 'https://webdev.ung.uz' + str(self.ru_fileurl.url)
            return str(url)
        else:
            return None 
    def fileurl_en(self):
        if self.en_fileurl:
            url = 'https://webdev.ung.uz' + str(self.en_fileurl.url)
            return str(url)
        else:
            return None
    def fileurl_uz(self):
        if self.uz_fileurl:
            url = 'https://webdev.ung.uz' + str(self.uz_fileurl.url)
            return str(url)
        else:
            return None



    @property
    def filesize_ru(self):
        if self.ru_fileurl:
            x = self.ru_fileurl.size
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
        else:
            return None
    
    @property
    def filesize_en(self):
        if self.en_fileurl:
            x = self.en_fileurl.size
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
        else:
            return None
    
    @property
    def filesize_uz(self):
        if self.uz_fileurl:
            x = self.uz_fileurl.size
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
        else:
            return None
    
    def __str__(self):
        return str(self.filename)

class Tender(models.Model):
    company = models.ForeignKey('CompanyModel', related_name='company_tenders', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    asosiy_talablar = RichTextField(blank=True, null=True)
    fileInfo = models.ForeignKey(FileTender, related_name='file_info', null=False, blank=False, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=datetime.now(), verbose_name="date_published")
    date_end = models.DateTimeField(default=datetime.now(),verbose_name="date_end")
    slug = models.SlugField(blank=False, unique=True)
    
    status = models.BooleanField("Is Open", default=True)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    @property
    def tenderlots(self):
        return self.tenderlot_set.all()

    class Meta:
        ordering = ['-date_published']

class TenderLot(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.BigIntegerField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    status = 'open'


    def __str__(self):
        return self.name

class CompanyModel(models.Model):
    name = models.CharField(max_length=350, null=True, blank=True)
    inn = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    clientBillNumber = models.CharField(max_length=450, null=True, blank=True)
    deliveryTerms = models.TextField(null=True, blank=True)
    deadline = models.TextField(null=True, blank=True)
    paymentTerms = models.TextField(null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_ends = models.DateTimeField(auto_now=True, verbose_name="date_ending")

    def __str__(self):
        return str(self.name)