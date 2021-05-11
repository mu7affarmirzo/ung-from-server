import pytz, os
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils import timezone

from uuid import uuid4

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'allfiles/files/{filename}'.format(
        title=str(instance.filename), filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)


class SubCategories(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='sub_category')
    subcategory = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.subcategory)

class Documents(models.Model):

    filename = models.CharField(max_length=500, null=False, blank=False)
    description = RichTextField(blank=True, null=True)
    sub_catory = models.ForeignKey(SubCategories, blank=True, null=True, on_delete=models.CASCADE, related_name='docs')
    fileurl_ru = models.FileField(upload_to=upload_location, null=True, blank=True)
    fileurl_en = models.FileField(upload_to=upload_location, null=True, blank=True)
    fileurl_uz = models.FileField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField()
    # slug = models.SlugField(blank=True, unique=True)
    url = models.URLField(max_length = 200, blank=True, null=True)

    class Meta:
        ordering = ['-date_published']

    def extension_ru(self):
        if self.fileurl_ru==None:
            extention = None
            return extention
        else:
            name, extension = os.path.splitext(self.fileurl_ru.name)
            return extension
    def extension_en(self):
        if self.fileurl_en == None:
            extention = None
            return extention
        else:
            name, extension = os.path.splitext(self.fileurl_en.name)
            return extension
    def extension_uz(self):
        if self.fileurl_uz == None:
            extention = None
            return extention
        else:
            name, extension = os.path.splitext(self.fileurl_uz.name)
            return extension


    @property
    def filesize_ru(self):
        if self.fileurl_ru in [None, '']:
            value = None
            return str(value)
        else:
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
        if self.fileurl_ru in [None, '']:
            value = None
            return value
        else:
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
        if self.fileurl_ru in [None, '']:
            value = None
            return value
        else:
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

    

class OffCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class WithoutCategory(models.Model):
    subcategory  = models.ForeignKey(OffCategory, blank=True, null=True,on_delete=models.CASCADE, related_name='without')
    filename = models.CharField(max_length=100, null=False, blank=False)
    description = RichTextField(blank=True, null=True)
    fileurl_ru = models.FileField(upload_to=upload_location, null=False, blank=False)
    fileurl_en = models.FileField(upload_to=upload_location, null=False, blank=False)
    fileurl_uz = models.FileField(upload_to=upload_location, null=False, blank=False)
    
    date_published = models.DateTimeField()
    # slug = models.SlugField(blank=True, unique=True)
    url = models.URLField(max_length = 200, blank=True, null=True)

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
        return str(self.subcategory)

    class Meta:
        ordering = ['-date_published']