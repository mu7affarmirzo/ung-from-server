from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import (
    Tender,
    TenderLot,
    CompanyModel,
    FileTender,
    # FileInfo,
)

class FilesAdmin(TranslationAdmin):
    pass
admin.site.register(FileTender, FilesAdmin)


class CompaniesAdmin(TranslationAdmin):
    pass
admin.site.register(CompanyModel, CompaniesAdmin)


class TenderAdminForm(forms.ModelForm):

    class Meta:
        model = Tender
        fields = '__all__'

class TenderLotAdmin(admin.StackedInline):
    model = TenderLot

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [TenderLotAdmin]

    class Meta:
        model = Tender

@admin.register(TenderLot)
class TenderLotAdmin(admin.ModelAdmin):
    pass
