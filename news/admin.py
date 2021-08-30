from django.contrib import admin
from django import forms

from news.models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# this is for ratingData
class RatingsCustomAdmin(admin.ModelAdmin):
    list_display = ('text_ru', 'text_en', 'text_uz')
    class Meta:
        verbose_name = "ratings"
class RatingsAdmin(RatingsCustomAdmin, TranslationAdmin):
    pass
admin.site.register(RatingData, RatingsAdmin)


# this is for News
class NewsCustomAdmin(admin.ModelAdmin):
    list_display = ('news_title_uz', 'date_published', 'status', 'youth_stat')
    class Meta:
        verbose_name = "users"


class NewsAdmin(NewsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(UngNewsModel, NewsAdmin)


class ComplianceNewsCustomAdmin(admin.ModelAdmin):
    list_display = ('news_title_uz', 'date_published')

    # class Meta:
    #     verbose_name = "users"


class ComplianceNewsAdmin(ComplianceNewsCustomAdmin, TranslationAdmin):
    pass
admin.site.register(ComplNewsModel, ComplianceNewsAdmin)

