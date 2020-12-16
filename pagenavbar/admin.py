from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import MenuCategories, MenuSubCategory

class MenuCategoryAdmin(TranslationAdmin):
    pass
admin.site.register(MenuCategories, MenuCategoryAdmin)


class MenuSubCategoryAdmin(TranslationAdmin):
    pass
admin.site.register(MenuSubCategory, MenuSubCategoryAdmin)