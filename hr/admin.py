from django.contrib import admin
from .models import *


class EducationInline(admin.StackedInline):
    model = EducationInfoModel


class ExtraEducationInline(admin.StackedInline):
    model = ExtraEducationInfoModel


class LanguagesInline(admin.StackedInline):
    model = LanguagesModel


class SkillsInline(admin.StackedInline):
    model = SkillsModel


class ExperienceInline(admin.StackedInline):
    model = ExperienceModel


class AdditionalInformationInline(admin.StackedInline):
    model = AdditionalInformationModel


@admin.register(UploadCv)
class UploadCVAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'position', 'phone_number')
    inlines = [
        EducationInline,
        ExtraEducationInline,
        LanguagesInline,
        SkillsInline,
        ExperienceInline,
        AdditionalInformationInline,
    ]




#
# class CVAdmin(admin.ModelAdmin):
#     inlines = [EducationInfoModel]
#
#     class Meta:
#         model = UploadCv
#
# class CVCustomAdmin(CVAdmin, TranslationAdmin):
#     pass
# admin.site.register(Tender, TenderCustomAdmin)
#
#
# class TenderLotAdmin(TranslationAdmin):
#     pass
# admin.site.register(TenderLot, TenderLotAdmin)