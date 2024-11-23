from rest_framework import serializers
from .models import FaqAilab


class FaqAilabSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAilab
        fields = '__all__'
