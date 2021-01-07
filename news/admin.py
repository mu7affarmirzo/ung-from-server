from django.contrib import admin
from django import forms

from news.models import UngNewsModel
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class NewsCustomAdmin(admin.ModelAdmin):
    list_display = ('news_title_uz', 'date_published', 'status')
class NewsAdmin(NewsCustomAdmin, TranslationAdmin):
    pass
admin.site.register(UngNewsModel, NewsAdmin)



# @admin.register(UngNewsModel)
# class UngNewsModelAdmin(TranslationAdmin):
#     news_body_ru = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
#     news_body_uz = forms.CharField(label='Tekst', widget=CKEditorUploadingWidget())
#     news_body_en = forms.CharField(label='Text', widget=CKEditorUploadingWidget())

#     class Meta:
#         model = UngNewsModel
#         fields = '__all__'

