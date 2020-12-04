from modeltranslation.translator import register, TranslationOptions
from .models import TenderLot, Tender

@register(TenderLot)
class TenderLotTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Tender)
class TenderTranslationOptions(TranslationOptions):
    fields = ('title', 'asosiy_talablar')