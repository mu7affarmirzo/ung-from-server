from rest_framework import serializers
from .models import Category, SubCategories, Documents

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = Category
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id'
            ]

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = [
            'category',
            'subcategory_ru', 'subcategory_en', 'subcategory_uz',
            ]

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = [
            'title_ru', 'title_en', 'title_uz',
            'body_ru', 'body_en', 'body_uz', 
            'sub_catory',
            'fileurl_ru', 'fileurl_en', 'fileurl_uz',
            'url',
            'extension_ru', 'extension_en', 'extension_uz',
            'filesize_ru', 'filesize_en', 'filesize_uz', 
            ]