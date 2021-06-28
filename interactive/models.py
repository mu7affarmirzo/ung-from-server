from django.db import models
from datetime import datetime 
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver

from uuid import uuid4

from news.models import UngNewsModel

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'allfiles/applic-files/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class ApplicationForm(models.Model):
    full_name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField()
    number = models.CharField(max_length=500, blank=True, null=True)
    birth_date = models.CharField(max_length=500, blank=True, null=True)
    topic = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=upload_location, blank=True, null=True)
    date_published = models.DateTimeField(default=datetime.now(),verbose_name="date_published")

    status = models.BooleanField(verbose_name="O'qilgan", default=False)

    def __str__(self):
        return str(self.topic)




class MailsModel(models.Model):
    full_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField()
    date_subscribed = models.DateTimeField(default=datetime.now(),verbose_name="date_subscribed")


    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ('-date_subscribed',)

# @receiver(post_save, sender=UngNewsModel)
# def send_news_via_email(sender, instance, created, **kwargs):
#     if created:
#         news_title = instance.news_title if instance.news_title else "no title given"
#         message = 'Here is our new post!\n' + news_title
#         subject = "news added"
#         from_email = settings.EMAIL_HOST_USER
#         send_mail(
#             subject,
#             message,
#             from_email,
#             ['m.choriev@student.inha.uz', 'm.choriev@ung.uz '],
#             fail_silently=False,
#         )


# post_save.connect(send_news, sender=MailsModel)