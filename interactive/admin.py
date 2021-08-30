from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

import csv, datetime
from django.http import HttpResponse
from csvexport.actions import csvexport


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta

        response = HttpResponse(content_type='application/vnd.ms-excel')
        
        response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(meta)
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        writer.writerow(['id','F.I.O', 'Manzil', 'email', 'Telefon raqami', 'Tug\'ilgan sanasi','Mavzu', 'Bayon', 'Hujjat', 'Qoldirilgan vaqt', 'Status'])
        field_names = ['id', 'full_name', 'address', 'email', 'number', 'birth_date', 'topic', 'text', 'file', 'date_published', 'status']
        # writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, str(field)) for field in field_names])

        return response

    export_as_csv.short_description = "Excelga o'girish"



def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename{}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response

export_to_csv.short_description = 'Export to CSV'



@admin.register(ApplicationForm)
class ApplicationAdmin(admin.ModelAdmin, ExportCsvMixin):

    list_display = ("full_name", "number", "email", "topic", "date_published", "status")
    list_filter = ("date_published", "status",)

    actions = [export_to_csv]
    # actions = ["export_as_csv"]
    # actions = [csvexport]


admin.site.register(MailsModel)
# admin.site.register(OptionsModel)




class QuestionsCustomAdmin(admin.ModelAdmin):
    list_display = ('full_text_ru', 'full_text_en', 'full_text_uz')
    class Meta:
        verbose_name = "questions"
class QuestionsAdmin(QuestionsCustomAdmin, TranslationAdmin):
    pass
admin.site.register(QuestionaireModel, QuestionsAdmin)


class OptionsCustomAdmin(admin.ModelAdmin):
    list_display = ('option_ru', 'option_en', 'option_uz')
    class Meta:
        verbose_name = "options"
class OptionsAdmin(OptionsCustomAdmin, TranslationAdmin):
    pass
admin.site.register(OptionsModel, OptionsAdmin)