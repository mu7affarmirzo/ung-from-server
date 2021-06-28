from rest_framework import serializers
from .models import ApplicationForm

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