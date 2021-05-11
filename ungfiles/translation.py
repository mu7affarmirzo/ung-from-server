from modeltranslation.translator import register, TranslationOptions
from .models import (
    SubCategories, 
    Category, 
    Documents,
    OffCategory,
    WithoutCategory
)

@register(SubCategories)
class SubCategoriesTranslationOptions(TranslationOptions):
    fields = (
        'subcategory',
        )

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Documents)
class DocumentsTranslationOptions(TranslationOptions):
    fields = ('filename', 'description')

@register(OffCategory)
class OffCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(WithoutCategory)
class WithoutCategoryTranslationOptions(TranslationOptions):
    fields = ('filename', 'description')
