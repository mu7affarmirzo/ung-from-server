from rest_framework import serializers
from .models import *


class AdditionalInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformationModel
        fields = [
            "starting_date",
            "salary",
            "driver_licence",
            "type",
            "confirmation",
            "how_did_you_find",
            "recommendations",
        ]


class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = [
            "date_started",
            "date_ended",
            "company_name",
            "position",
            "achievements",
            "reason",
            "recommendations",
        ]


class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SkillsModel
        fields = [
            "skill_name",
            "level",
        ]


class LanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LanguagesModel
        fields = [
            "lang_name",
            "writing",
            "reading",
            "speaking",
        ]


class ExtraEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExtraEducationInfoModel
        fields = [
            "place",
            "speciality",
            "date_started",
            "date_ended",
        ]


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationInfoModel
        fields = [
            "place",
            "faculty",
            "speciality",
            "date_started",
            "date_ended",
            # "upploadcv"
        ]


class CVUploadsSerializers(serializers.ModelSerializer):
    additional = AdditionalInformationSerializers(many=True)
    experience = ExperienceSerializers(many=True)
    skills = SkillsSerializers(many=True)
    language = LanguagesSerializers(many=True)
    extraeducation = ExtraEducationSerializers(many=True)
    education = EducationSerializers(many=True)

    class Meta:
        model = UploadCv
        fields = [
            'surname',
            'name',
            'fathers_name',
            'date_of_birth',
            'marriage_status',
            'kids',
            'address',
            'phone_number',
            'email',
            'entry_type',
            'city',
            'position',
            'education',
            'extraeducation',
            'language',
            'skills',
            'experience',
            'additional',
        ]

    def update(self, instance, validated_data):
        education = validated_data.pop('education')
        extraeducation = validated_data.pop('extraeducation')
        language = validated_data.pop('language')
        skills = validated_data.pop('skills')
        experience = validated_data.pop('experience')
        additional = validated_data.pop('additional')
        upploadcv = UploadCv.objects.create(**validated_data)

        for edu in education:
            EducationInfoModel.objects.create(**edu, upploadcv=upploadcv)
        for exedu in extraeducation:
            ExtraEducationInfoModel.objects.create(**exedu, upploadcv=upploadcv)
        for lan in language:
            LanguagesModel.objects.create(**lan, upploadcv=upploadcv)
        for skill in skills:
            SkillsModel.objects.create(**skill, upploadcv=upploadcv)
        for exp in experience:
            ExperienceModel.objects.create(**exp, upploadcv=upploadcv)
        for addit in additional:
            AdditionalInformationModel.objects.create(**addit, upploadcv=upploadcv)
        return upploadcv