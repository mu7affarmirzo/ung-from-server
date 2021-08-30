from django.db import models
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


class UploadCv(models.Model):
    surname = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    fathers_name = models.CharField(max_length=500, null=True, blank=True)
    date_of_birth = models.CharField(max_length=500, null=True, blank=True)
    marriage_status = models.CharField(max_length=500, null=True, blank=True)
    kids = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    entry_type = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'CV yuborganlar ro`yxati'
        verbose_name_plural = 'CV yuborganlar ro`yxati'
    @property
    def education(self):
        return self.educationinfomodel_set.all()

    @property
    def extraeducation(self):
        return self.extraeducationinfomodel_set.all()

    @property
    def language(self):
        return self.languagemodel_set.all()

    @property
    def skill(self):
        return self.skillsmodel_set.all()

    @property
    def skill(self):
        return self.skillsmodel_set.all()

    @property
    def experience(self):
        return self.experiencemodel_set.all()


    @property
    def additional(self):
        return self.additionalinformationmodel_set.all()

    def __str__(self):
        return self.name + ' ' + self.surname


class EducationInfoModel(models.Model):
    upploadcv = models.ForeignKey(UploadCv, related_name='education', on_delete=models.CASCADE)
    place = models.CharField(max_length=500, null=True, blank=True)
    faculty = models.CharField(max_length=500, null=True, blank=True)
    speciality = models.CharField(max_length=500, null=True, blank=True)
    date_started = models.CharField(max_length=500, null=True, blank=True)
    date_ended = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.place) + '/' + str(self.faculty)

    class Meta:
        verbose_name = 'Ma\'lumoti'
        verbose_name_plural = 'Ma\'lumoti'


class ExtraEducationInfoModel(models.Model):
    upploadcv = models.ForeignKey(UploadCv, related_name='extraeducation', on_delete=models.CASCADE)
    place = models.CharField(max_length=500, null=True, blank=True)
    speciality = models.CharField(max_length=500, null=True, blank=True)
    date_started = models.CharField(max_length=500, null=True, blank=True)
    date_ended = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.place + '/' + self.speciality

    class Meta:
        verbose_name = 'Qo‘shimcha ma’lumot (malaka oshirish, kurslar, boshqalar)'
        verbose_name_plural = 'Qo‘shimcha ma’lumot (malaka oshirish, kurslar, boshqalar)'


class LanguagesModel(models.Model):
    upploadcv = models.ForeignKey(UploadCv, related_name='language', on_delete=models.CASCADE)
    lang_name = models.CharField(max_length=500, null=True, blank=True)
    writing = models.IntegerField(null=True, blank=True)
    reading = models.IntegerField(null=True, blank=True)
    speaking = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.lang_name

    class Meta:
        verbose_name = 'Xorijiy tillarni bilish'
        verbose_name_plural = 'Xorijiy tillarni bilish'
#
#
class SkillsModel(models.Model):
    upploadcv = models.ForeignKey(UploadCv, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=500, null=True, blank=True)
    level = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.skill_name)

    class Meta:
        verbose_name = 'Komputerda ishlash ko‘nikmalari'
        verbose_name_plural = 'Komputerda ishlash ko‘nikmalari'
#
#
class ExperienceModel(models.Model):
    upploadcv = models.ForeignKey(UploadCv, related_name='experience', on_delete=models.CASCADE)
    date_started = models.CharField(max_length=500, null=True, blank=True)
    date_ended = models.CharField(max_length=500, null=True, blank=True)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    achievements = models.CharField(max_length=500, null=True, blank=True)
    reason = models.CharField(max_length=500, null=True, blank=True)
    recommendations = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.company_name) + "/" + str(self.position)

    class Meta:
        verbose_name = 'Mehnat faoliyati'
        verbose_name_plural = 'Mehnat faoliyati'
#
#
class AdditionalInformationModel(models.Model):
    upploadcv = models.ForeignKey(UploadCv, related_name='additional', on_delete=models.CASCADE)
    starting_date = models.CharField(max_length=500, null=True, blank=True)
    salary = models.CharField(max_length=500, null=True, blank=True)
    driver_licence = models.BooleanField(default=False)
    type = models.CharField(max_length=500, null=True, blank=True)
    confirmation = models.CharField(max_length=500, null=True, blank=True)
    how_did_you_find = models.CharField(max_length=500, null=True, blank=True)
    recommendations = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "Qo'shimcha ma'lumotlar"

    class Meta:
        verbose_name = 'Qo‘shimcha ma’lumotlar'
        verbose_name_plural = 'Qo‘shimcha ma’lumotlar'

