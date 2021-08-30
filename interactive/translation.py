from modeltranslation.translator import register, TranslationOptions
from .models import QuestionaireModel, OptionsModel

@register(QuestionaireModel)
class QuestionaireTranslationOptions(TranslationOptions):
    fields = ('full_text', )


@register(OptionsModel)
class OptionsTranslationOptions(TranslationOptions):
    fields = ('option', )