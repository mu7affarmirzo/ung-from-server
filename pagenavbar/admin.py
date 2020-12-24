from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import MenuCategories, MenuSubCategory, ChildSubCategory

class MenuCategoryAdmin(TranslationAdmin):
    pass
admin.site.register(MenuCategories, MenuCategoryAdmin)


class MenuSubCategoryAdmin(TranslationAdmin):
    pass
admin.site.register(MenuSubCategory, MenuSubCategoryAdmin)

class ChildSubCategoryAdmin(TranslationAdmin):
    pass
admin.site.register(ChildSubCategory, ChildSubCategoryAdmin)