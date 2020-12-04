from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField



def upload_location(instance, filename):
    file_path = 'news_archive/{news_title}-{filename}'.format(
        news_title=str(instance.news_title), filename=filename
    )
    return file_path

class UngNewsModel(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    news_title = models.CharField(max_length=100, null=False, blank=False)
    news_body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="slider")

    def __str__(self):
        return self.news_title

@receiver(post_delete, sender = UngNewsModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify("-" + instance.news_title)

pre_save.connect(pre_save_news_post_receiver, sender=UngNewsModel)