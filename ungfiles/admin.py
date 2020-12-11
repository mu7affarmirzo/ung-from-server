from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, SubCategories, Documents
# TypeFiles, AllFiles

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass

# @admin.register(SubCategories)
# class SubCategoriesAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Documents)
# class DocmentsAdmin(admin.ModelAdmin):
#     pass

class CategoryAdmin(TranslationAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class DocumentsAdmin(TranslationAdmin):
    pass
admin.site.register(Documents, DocumentsAdmin)


class SubCategoriesAdmin(TranslationAdmin):
    pass
admin.site.register(SubCategories, SubCategoriesAdmin)