from modeltranslation.translator import register, TranslationOptions
from .models import SubCategories, Category, Documents

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
