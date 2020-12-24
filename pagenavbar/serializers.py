from rest_framework import serializers
from .models import MenuCategories, MenuSubCategory, ChildSubCategory
from ungfiles.models import Category
from ungfiles.serializers import SubCategoriesSerializer, CategorySerializer, ChildsForNavbar
from tenders.models import CompanyModel
from tenders.serializers import TenderCompaniesSerializer


class ChildSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = ChildSubCategory
        fields = [
            'menusubcategory',
            'name_ru', 'name_en', 'name_uz',
            'id',
            'url',
            ]

class ForChildSerializer(serializers.ModelSerializer):
    child_sub_category = ChildSerializer(many=True)
    class Meta:
        model = MenuSubCategory
        fields = [
            'name_ru', 'name_en', 'name_uz',
            # 'id',
            'url',
            # 'redir',
            'child_sub_category',
            ]

class CategoryMenuSerializer(serializers.ModelSerializer):
    child_sub_category = ChildSerializer()
    id = serializers.IntegerField(required=True)
    class Meta:
        model = MenuCategories
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'img',
            'url',
            'id',
            'child_sub_category',
            ]


class SubCategoryMenuSerializer(serializers.ModelSerializer):
    child_sub_category = ChildSerializer(many=True)
    redir = ChildsForNavbar()
    id = serializers.IntegerField(required=True)
    class Meta:
        model = MenuSubCategory
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'id',
            'url',
            'redir',
            'child_sub_category',
            ]

class MenuCatSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryMenuSerializer(many=True)
    redir = ChildsForNavbar()
    id = serializers.IntegerField(required=True)
    class Meta:
        model = MenuCategories
        fields = [
            'name_ru', 'name_en', 'name_uz',
            'img',
            'url',
            'id',
            'sub_category',
            'redir'
            ]