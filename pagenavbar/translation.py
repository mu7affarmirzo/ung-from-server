from modeltranslation.translator import register, TranslationOptions
from .models import MenuSubCategory, MenuCategories, ChildSubCategory

@register(MenuSubCategory)
class SubCategoriesTranslationOptions(TranslationOptions):
    fields = (
        'name',
        )

@register(MenuCategories)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ChildSubCategory)
class ChildTranslationOptions(TranslationOptions):
    fields = ('name',)