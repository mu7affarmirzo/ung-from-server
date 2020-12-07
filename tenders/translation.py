from modeltranslation.translator import register, TranslationOptions
from .models import TenderLot, Tender, CompanyModel

@register(TenderLot)
class TenderLotTranslationOptions(TranslationOptions):
    fields = (
        'name', 'description', 'unit')

@register(Tender)
class TenderTranslationOptions(TranslationOptions):
    fields = ('title', 'asosiy_talablar')

@register(CompanyModel)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'deliveryTerms', 'deadline', 'paymentTerms')