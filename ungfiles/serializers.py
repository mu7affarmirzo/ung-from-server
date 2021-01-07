from rest_framework import serializers
from .models import Category, SubCategories, Documents, OffCategory, WithoutCategory

class SubCategoriesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = SubCategories
        fields = [
            'category',
            'subcategory_ru', 'subcategory_en', 'subcategory_uz',
            'id',
            ]

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = Category
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            ]

class ChildCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = Category
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            ]

class ChildsForNavbar(serializers.ModelSerializer):
    sub_category = SubCategoriesSerializer(many=True)
    id = serializers.IntegerField(required=True)
    class Meta: 
        model = Category
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            'sub_category',
            ]

# class SubCategoriesSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=True)
#     class Meta:
#         model = SubCategories
#         fields = [
#             'category',
#             'subcategory_ru', 'subcategory_en', 'subcategory_uz',
#             'id',
#             ]



class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = [
            'filename_ru', 'filename_en', 'filename_uz',
            'description_ru', 'description_en', 'description_uz', 
            'sub_catory',
            'fileurl_ru', 'fileurl_en', 'fileurl_uz',
            'url',
            'extension_ru', 'extension_en', 'extension_uz',
            'filesize_ru', 'filesize_en', 'filesize_uz', 
            'date_published'
            ]
        depth=1

class FilterDocumentsSerializer(serializers.ModelSerializer):
    docs = DocumentsSerializer(many=True)
    id = serializers.IntegerField(required=True)
    class Meta: 
        model = SubCategories
        fields = [
            'category',
            'subcategory_ru', 'subcategory_en', 'subcategory_uz',
            'id',
            'docs',
            ]


class WithoutDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithoutCategory
        fields = [
            'filename_ru', 'filename_en', 'filename_uz',
            'description_ru', 'description_en', 'description_uz', 
            # 'sub_catory',
            'fileurl_ru', 'fileurl_en', 'fileurl_uz',
            'url',
            'extension_ru', 'extension_en', 'extension_uz',
            'filesize_ru', 'filesize_en', 'filesize_uz', 
            ]

class OffFilterDocumentsSerializer(serializers.ModelSerializer):
    without = WithoutDocumentsSerializer(many=True)
    id = serializers.IntegerField(required=True)
    class Meta: 
        model = OffCategory
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            'without',
            ]