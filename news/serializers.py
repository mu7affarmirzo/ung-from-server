from rest_framework import serializers
from .models import UngNewsModel, RatingData
from tenders.models import Tender
from .translation import UngNewsTranslationOptions

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingData
        fields = [
            'id',
            "icon",
            "text_ru",
            "text_en",
            "text_uz",
            "number",
        ]

class UngNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields = [
            'news_title_ru', 'news_title_en', 'news_title_uz', 
            'news_body_ru', 'news_body_en', 'news_body_uz',
            'image_ru','image_en','image_uz', 
            'date_published',
            'date_updated', 
            'slug',
            'status',
            'slid',
            'UrlDirection',
            # 'newsUrl'
            ]

class UngNewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields = [
            'news_title_ru', 'news_title_en', 'news_title_uz', 
            'image_ru','image_en','image_uz', 
            'date_updated', 
            'slug',
            'UrlDirection',
            # 'newsUrl'
            ]

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields =  '__all__'


class SeachNewsSerializer(serializers.ModelSerializer):
    title_uz = serializers.CharField(source='news_title_uz')
    title_ru = serializers.CharField(source='news_title_ru')
    title_en = serializers.CharField(source='news_title_en')
    class Meta:
        model = UngNewsModel
        fields = [
            'title_ru', 'title_en', 'title_uz', 
            'UrlDirection',
            ]

class SeachTendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = [
            'title_ru', 'title_en', 'title_uz', 
            'UrlDirection',
            ]