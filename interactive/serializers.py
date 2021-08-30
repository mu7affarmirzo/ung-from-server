from django.db.models import fields
from rest_framework import serializers
from .translation import QuestionaireTranslationOptions, OptionsTranslationOptions
from .models import ApplicationForm, QuestionaireModel, OptionsModel

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = [
        'full_name',
        'address',
        'email',
        'number',
        'birth_date',
        'topic',
        'text',
        'file'
        ]


class QuestionaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionaireModel
        fields = "__all__"
        # fields = [
        #     'id',
        #     'votes_count',
        # ]

# tracks = serializers.StringRelatedField(many=True)

class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OptionsModel
        fields = "__all__"
        # fields = [
        #     'id',
        #     'votes_count',
        #     'options'
        # ]


class QuestionsSerializer(serializers.ModelSerializer):
    # options = serializers.StringRelatedField(many=True)
    options = OptionsSerializer(many=True, read_only=True)
    class Meta:
        model = QuestionaireModel
        # fields = "__all__"
        fields = [
            'id',
            'full_text_uz',
            'full_text_ru',
            'full_text_en',
            'votes_count',
            'options'
        ]


