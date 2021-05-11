from rest_framework import serializers
from .models import UngNewsModel, RatingData
from .translation import UngNewsTranslationOptions

from django.db import models
from django.db.models import CharField

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
            ]

class UngNewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields = [
            'news_title_ru', 'news_title_en', 'news_title_uz', 
            'image_ru','image_en','image_uz', 
            'date_published', 
            'date_updated',
            ]

# **************   NEWS FOR DIFFERENT LANGUAGES   ************
class RUnews(serializers.ModelSerializer):
    title = serializers.CharField(source='news_title_ru')
    image = serializers.ImageField(source='image_ru')
    class Meta:
        model = UngNewsModel
        fields = ['image', 'title','date_published', 'slug', 'mum_status', 'youth']

class RUnewsspesific(serializers.ModelSerializer):
    title = serializers.CharField(source='news_title_ru')
    image = serializers.ImageField(source='image_ru')
    news_body = serializers.CharField(source='news_body_ru')
    class Meta:
        model = UngNewsModel
        fields = ['image', 'title', 'news_body', 'date_published', 'slug']




class UZnews(serializers.ModelSerializer):
    title = serializers.CharField(source='news_title_uz')
    image = serializers.ImageField(source='image_uz')
    class Meta:
        model = UngNewsModel
        fields = ['image', 'title','date_published', 'slug', 'mum_status', 'youth']
        
class UZnewsspesific(serializers.ModelSerializer):
    title = serializers.CharField(source='news_title_uz')
    image = serializers.ImageField(source='image_uz')
    news_body = serializers.CharField(source='news_body_uz')
    class Meta:
        model = UngNewsModel
        fields = ['image', 'title', 'news_body', 'date_published', 'slug']




class ENnews(serializers.ModelSerializer):
    title = serializers.CharField(source='news_title_en')
    image = serializers.ImageField(source='image_en')
    class Meta:
        model = UngNewsModel
        fields = ['image', 'title','date_published', 'slug', 'mum_status', 'youth']


class ENnewsspesific(serializers.ModelSerializer):
    title = serializers.CharField(source='news_title_en')
    image = serializers.ImageField(source='image_en')
    news_body = serializers.CharField(source='news_body_en')
    class Meta:
        model = UngNewsModel
        fields = ['image', 'title', 'news_body', 'date_published', 'slug']

# *********** NEWS ENDS HERE ****************


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngNewsModel
        fields =  '__all__'