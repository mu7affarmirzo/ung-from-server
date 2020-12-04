from modeltranslation.translator import register, TranslationOptions
from .models import UngNewsModel

@register(UngNewsModel)
class UngNewsTranslationOptions(TranslationOptions):
    fields = ('news_title', 'news_body')