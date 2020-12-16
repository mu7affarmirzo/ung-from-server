from rest_framework import serializers
from .models import MenuCategories, MenuSubCategory
from ungfiles.models import Category
from ungfiles.serializers import SubCategoriesSerializer, CategorySerializer


class CategoryMenuSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = MenuCategories
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'img',
            'url',
            'id',
            ]


class SubCategoryMenuSerializer(serializers.ModelSerializer):
    redir = CategorySerializer()
    id = serializers.IntegerField(required=True)
    class Meta:
        model = MenuSubCategory
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            'redir',
            ]

class MenuCatSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryMenuSerializer(many=True)
    id = serializers.IntegerField(required=True)
    class Meta:
        model = MenuCategories
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'img',
            'url',
            'id',
            'sub_category',
            ]