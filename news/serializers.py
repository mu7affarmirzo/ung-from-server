from rest_framework import serializers
from .models import UngNewsModel, RatingData
from .translation import UngNewsTranslationOptions

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingData
        fields = '__all__'

class UngNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields = [
            'news_title_ru', 'news_title_en', 'news_title_uz', 
            'news_body_ru', 'news_body_en', 'news_body_uz',
            'image', 
            'date_published',
            'date_updated', 
            'slug',
            'status',
            'slid',
            ]

class UngNewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields = [
            'news_title_ru', 'news_title_en', 'news_title_uz', 
            'image', 
            'date_updated', 
            'slug',
            ]

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields =  '__all__'