from rest_framework import serializers
from .models import Tender, TenderLot, CompanyModel, FileTender

class TenderCompaniesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = CompanyModel
        fields = ['id',
            'name_ru', 'name_en', 'name_uz',
            'inn',
            'address_ru', 'address_en', 'address_uz',
            'phone',
            'clientBillNumber',
            'deliveryTerms_ru', 'deliveryTerms_en', 'deliveryTerms_uz',
            'deadline_ru', 'deadline_en', 'deadline_uz',
            'paymentTerms_ru', 'paymentTerms_en', 'paymentTerms_uz',
        ]
        
    
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
            # 'date_published',
            # 'date_ends',
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

class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileTender
        fields = [
            'filename_ru', 'filename_en', 'filename_uz',
            'fileurl_ru', 'fileurl_en', 'fileurl_uz',
            'description_ru', 'description_en', 'description_uz',
            'extension_ru', 'extension_en', 'extension_uz',
            'filesize_ru', 'filesize_en', 'filesize_uz',
            # 'urlfile_ru', 'urlfile_en', 'urlfile_uz',
        ]

class TenderSerializer(serializers.ModelSerializer):
    tenderlots = TenderLotSerializer(many=True)
    company = CompanyRequisitesSerializer()
    fileInfo = FileInfoSerializer()
    class Meta:
        model = Tender
        fields = [
            'company',
            'title_ru', 'title_en', 'title_uz',
            'asosiy_talablar_ru', 'asosiy_talablar_en', 'asosiy_talablar_uz',
            # 'file',
            'fileInfo',
            'date_published',
            'date_end',
            'tenderlots',
            'status',
            # 'filesize',
            'slug',
            # 'extension',
        ]

class TenderListSerializer(serializers.ModelSerializer):
    company = TenderCompaniesSerializer()
    class Meta:
        model = Tender
        fields = [
            'company',
            'title_ru', 'title_en', 'title_uz',
            'asosiy_talablar_ru', 'asosiy_talablar_en', 'asosiy_talablar_uz',
            # 'file',
            'date_published',
            'date_end',
            'status',
            # 'filesize',
            'slug',
        ]

    # def get_company(self, instance):
    #     tenders = instance.company.all().order_by('-date_published')
    #     return TenderCompaniesSerializer(tenders, many=True).data


class CoTenSerializer(serializers.ModelSerializer):
    tenders = TenderListSerializer(many=True)
    class Meta:
        model = CompanyModel
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            'tenders',
        ]