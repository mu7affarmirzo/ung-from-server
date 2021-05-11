from django.contrib import admin

from .models import CategoryModel, UploadedFileModel, SubCategoriesModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategoriesModel)
class SubCategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(UploadedFileModel)
class DocmentsAdmin(admin.ModelAdmin):
    pass
