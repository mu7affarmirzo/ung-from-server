from rest_framework import serializers
from .models import Tender, TenderLot, CompanyModel

class TenderCompaniesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = CompanyModel
        fields = ['name','id']

class CompanyRequisitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyModel
        fields = [
            'name',
            'inn',
            'address',
            'phone',
            'clientBillNumber',
            'deliveryTerms',
            'deadline',
            'paymentTerms',
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
                  'unit'
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

class CoTenSerializer(serializers.ModelSerializer):
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