from rest_framework import serializers
from .models import UngNewsModel
from .translation import UngNewsTranslationOptions

class UngNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields = [
            'news_title_ru', 'news_title_en', 'news_title_uz', 
            'news_body_ru', 'news_body_en', 'news_body_uz',
            'image', 
            'date_updated', 
            'slug',
            'status',
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