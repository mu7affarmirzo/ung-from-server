import os
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

def location_fo_upload(instance, filename):
    file_path = 'tender/files/{filename}'.format(
        filename=filename
    )
    return file_path

class FileTender(models.Model):
    filename = models.CharField(max_length=150, blank=True, null=True)
    # fileurl = models.FileField(upload_to=location_fo_upload, null=False, blank=False)
    fileurl_ru = models.FileField(upload_to=location_fo_upload, null=False, blank=False)
    fileurl_en = models.FileField(upload_to=location_fo_upload, null=False, blank=False)
    fileurl_uz = models.FileField(upload_to=location_fo_upload, null=False, blank=False)
    description = RichTextField(blank=True, null=True)
    
    def extension_ru(self):
        name, extension = os.path.splitext(self.fileurl_ru.name)
        return extension
    def extension_en(self):
        name, extension = os.path.splitext(self.fileurl_en.name)
        return extension
    def extension_uz(self):
        name, extension = os.path.splitext(self.fileurl_uz.name)
        return extension


    @property
    def filesize_ru(self):
        x = self.fileurl_ru.size
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
    
    @property
    def filesize_en(self):
        x = self.fileurl_en.size
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
    
    @property
    def filesize_uz(self):
        x = self.fileurl_uz.size
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
        return str(self.filename)

class Tender(models.Model):
    company = models.ForeignKey('CompanyModel', related_name='company_tenders', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    asosiy_talablar = RichTextField(blank=True, null=True)
    # file = models.FileField(upload_to=upload_location, null=False, blank=False)
    fileInfo = models.ForeignKey(FileTender, related_name='file_info', null=False, blank=False, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)
    
    status = models.BooleanField("Is Open", default=True)

#http://webdev.ung.uz/media/tender/files/This_is_some_text_for_testing_q1dgHiP.docx
#/media/tender/files/headline_shutterstock_243762007_taqmbuv.jpg
    # def extension(self):
    #     name, extension = os.path.splitext(self.file.name)
    #     return extension

    # @property
    # def filesize(self):
    #     x = self.file.size
    #     y = 512000
    #     if x < y:
    #         value = round(x / 1000, 2)
    #         ext = ' kb'
    #     elif x < y * 1000:
    #         value = round(x / 1000000, 2)
    #         ext = ' Mb'
    #     else:
    #         value = round(x / 1000000000, 2)
    #         ext = ' Gb'
    #     return str(value) + ext

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
    # status = models.BooleanField("Is Open", default=True, blank=True, null=True)
    # number = models.FloatField(blank=True, null=True)
    number = '5'
    status = 'open'


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
    # company_slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return str(self.name)