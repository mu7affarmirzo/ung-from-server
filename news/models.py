from django.db import models

from django.db.models.signals import pre_save, post_delete, post_save
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime 
from django.utils.timezone import now
import random as r

from django.core.mail import send_mail


from uuid import uuid4

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'news_archive/{filename}'.format(
        # news_title=str(instance.news_title), 
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class RatingData(models.Model):
    class Meta:
        verbose_name = "Reyting ikonka"
        verbose_name_plural = "Reyting ikonkalar"

    icon = models.ImageField(upload_to=upload_location, null=False, blank=False)
    text = models.TextField(null=True, blank=True)
    number = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.text)


class UngNewsModel(models.Model):

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    news_title = models.TextField(null=True, blank=True)
    news_body = RichTextField(blank=True, null=True)
    image_uz = models.ImageField(upload_to=upload_location, null=True, blank=True)
    image_ru = models.ImageField(upload_to=upload_location, null=True, blank=True)
    image_en = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(default=datetime.now(),verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="slider")
    youth_stat = models.BooleanField(verbose_name="youth_union")
    # newsUrl = 'news/'+str(slug)

    def slid(self):
        if self.status == True:
            return int("1")
        else:
            return int("0")

    def youth(self):
        if self.youth_stat == True:
            return int("1")
        else:
            return int("0")

    def UrlDirection(self):
        newsUrl = 'news/'+str(self.slug)
        return newsUrl


    def __str__(self):
        return self.news_title


class ComplNewsModel(models.Model):

    class Meta:
        verbose_name = "Compliance Yangiliklar"
        verbose_name_plural = "Compliance Yangiliklar"

    news_title = models.TextField(null=True, blank=True)
    news_body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(default=datetime.now(),verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)

    def UrlDirection(self):

        newsUrl = 'compliance/news/'+str(self.slug)
        return newsUrl

    def __str__(self):
        return self.news_title


@receiver(post_save, sender=UngNewsModel)
def send_news_via_email(sender, instance, created, **kwargs):
    if created:
        news_title = instance.news_title if instance.news_title else "no title given"
        message = 'Here is our new post!\n' + news_title
        subject = "news added"
        from_email = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message,
            from_email,
            ['m.choriev@student.inha.uz', 'm.choriev@ung.uz'],
            fail_silently=False,
        )

@receiver(post_delete, sender = UngNewsModel)
def submission_delete(sender, instance, **kwargs):
    instance.image_ru.delete(False)
    instance.image_en.delete(False)
    instance.image_uz.delete(False)

def pre_save_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))

pre_save.connect(pre_save_news_post_receiver, sender=UngNewsModel)


def pre_save_compl_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))

pre_save.connect(pre_save_compl_news_post_receiver, sender=ComplNewsModel)

# def upload_location(instance, filename):
#     ext = filename.split('.')[-1]
#     file_path = 'news_archive/{filename}'.format(
#         filename='{}.{}'.format(uuid4().hex, ext)
#     )
#     return file_path