from rest_framework import serializers
from .models import Tender, TenderLot, CompanyModel

class TenderCompaniesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = CompanyModel
        fields = ['name_ru', 'name_en', 'name_uz',
        'id']
    
class CompanyRequisitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyModel
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'inn',
            'address_ru', 'address_en', 'address_uz',
            'phone',
            'clientBillNumber',
            'deliveryTerms_ru', 'deliveryTerms_en', 'deliveryTerms_uz',
            'deadline_ru', 'deadline_en', 'deadline_uz',
            'paymentTerms_ru', 'paymentTerms_en', 'paymentTerms_uz',
            'date_published',
            'date_ends',
        ]

class TenderLotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = TenderLot
        fields = ['tender',
                  'name_ru', 'name_en', 'name_uz',
                  'description_ru', 'description_en', 'description_uz',
                  'price',
                  'id',
                  'unit_ru', 'unit_en', 'unit_uz',
                  'number',
                  'status',
                  ]

class TenderSerializer(serializers.ModelSerializer):
    tenderlots = TenderLotSerializer(many=True)
    company = CompanyRequisitesSerializer()
    class Meta:
        model = Tender
        fields = [
            'company',
            'title_ru', 'title_en', 'title_uz',
            'asosiy_talablar_ru', 'asosiy_talablar_en', 'asosiy_talablar_uz',
            'file',
            'date_published',
            'tenderlots',
            'status',
            'filesize',
            'slug',
            'extension',
        ]

class TenderListSerializer(serializers.ModelSerializer):
    company = TenderCompaniesSerializer()
    class Meta:
        model = Tender
        fields = [
            'company',
            'title_ru', 'title_en', 'title_uz',
            'asosiy_talablar_ru', 'asosiy_talablar_en', 'asosiy_talablar_uz',
            'file',
            'date_published',
            'status',
            'filesize',
            'slug',
        ]


# class FroCompTenderListSerializer(serializers.ModelSerializer):
#     tenderlots = TenderLotSerializer(many=True)
#     class Meta:
#         model = Tender
#         fields = [
#             'title_ru', 'title_en', 'title_uz',
#             'asosiy_talablar_ru', 'asosiy_talablar_en', 'asosiy_talablar_uz',
#             'file',
#             'date_published',
#             'tenderlots',
#             'status',
#             'filesize',
#             'slug',
#             'extension',
#         ]

class CoTenSerializer(serializers.ModelSerializer):
    tenders = TenderListSerializer(many=True)
    class Meta:
        model = CompanyModel
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            'tenders',
        ]

# class TendersInsideCompanies(serializers.ModelSerializer):
#     class Meta:
#         model = Tender
#         fields = [
#             'title_ru', 'title_en', 'title_uz',
#             'asosiy_talablar_ru', 'asosiy_talablar_en', 'asosiy_talablar_uz',
#             'file',
#             'date_published',
#             'status',
#             'filesize',
#             'slug',
#         ]

# class CompaniesWithTenders(serializers.ModelSerializer):
#     tenders = TendersInsideCompanies(many=True)
#     class Meta:
#         model = CompanyModel
#         fields = [
#             'name_ru', 'name_en', 'name_uz',
#             'id',
#             'tenders',
#         ]
