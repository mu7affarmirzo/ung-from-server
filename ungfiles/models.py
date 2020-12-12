import pytz, os
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils import timezone


def upload_location(instance, filename):
    file_path = 'allfiles/files/{filename}'.format(
        title=str(instance.filename), filename=filename
    )
    return file_path


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)


class SubCategories(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    subcategory = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.subcategory)

class Documents(models.Model):

    filename = models.CharField(max_length=100, null=False, blank=False)
    description = RichTextField(blank=True, null=True)
    sub_catory = models.ForeignKey(SubCategories, blank=True, null=True, on_delete=models.CASCADE, related_name='docs')
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
        return str(self.filename)