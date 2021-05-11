from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField

from ungfiles.models import *
from tenders.models import *

def upload_location(instance, filename):
    file_path = 'static/menu/{filename}'.format(
        filename=filename
    )
    return file_path

class MenuCategories(models.Model):
    name = models.CharField(max_length=250, null=True,blank=True)
    url = models.CharField(max_length=250, null=True,blank=True)
    img = models.ImageField(upload_to=upload_location, null=False, blank=False)
    redir = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)


class MenuSubCategory(models.Model):
    menucategory = models.ForeignKey(MenuCategories, on_delete=models.CASCADE, blank=True, null=True, related_name='sub_category')
    name = models.CharField(max_length=250, null=True,blank=True)
    url = models.CharField(max_length=250, null=True,blank=True)
    redir = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class ChildSubCategory(models.Model):
    menusubcategory = models.ForeignKey(MenuSubCategory, on_delete=models.CASCADE, blank=True, null=True, related_name='child_sub_category')
    name = models.CharField(max_length=250, null=True,blank=True)
    url = models.CharField(max_length=250, null=True,blank=True)
    # redir = models.ForeignKey(*, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)
