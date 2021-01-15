from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime 
from django.utils.timezone import now


from uuid import uuid4

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'news_archive/{filename}'.format(
        # news_title=str(instance.news_title), 
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path

# def ratings_location(instance, filename):
#     ext = filename.split('.')[-1]
#     file_path = 'news_archive/ratings/{filename}'.format(
#         news_title=str(instance.news_title), filename='{}.{}'.format(uuid4().hex, ext)
#     )
#     return file_path


class RatingData(models.Model):
    class Meta:
        verbose_name = "Reyting ikonka"
        verbose_name_plural = "Reyting ikonkalar"

    icon = models.ImageField(upload_to=upload_location, null=False, blank=False)
    text = models.TextField(null=True, blank=True)
    number = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.text)
    
# const ratingData = [
#   {
#     Icon: <ProfitIcon />,
#     text: "Share of Uzbekneftegaz in GDP of Uzbekistan",
#     number: 10946,
#   },
#   {
#     Icon: <WorkerIcon />,
#     text: "Total staff",
#     number: 50000,
#   },
#   {
#     Icon: <HandsIcon />,
#     text: "Совместных предприятий",
#     number: 14,
#   },
# ];


class UngNewsModel(models.Model):

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    news_title = models.TextField(null=False, blank=False)
    news_body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(default=datetime.now(),verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="slider")
    youth_stat = models.BooleanField(verbose_name="youth_union")

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


    def __str__(self):
        return self.news_title

@receiver(post_delete, sender = UngNewsModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify("-" + instance.news_title)

pre_save.connect(pre_save_news_post_receiver, sender=UngNewsModel)