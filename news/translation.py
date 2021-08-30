from modeltranslation.translator import register, TranslationOptions
from .models import UngNewsModel, RatingData, ComplNewsModel

@register(RatingData)
class RatingsTranslationOptions(TranslationOptions):
    fields = ('text', )

@register(UngNewsModel)
class UngNewsTranslationOptions(TranslationOptions):
    fields = ('news_title', 'news_body')

@register(ComplNewsModel)
class ComplianceNewsTranslationOptions(TranslationOptions):
    fields = ('news_title', 'news_body')