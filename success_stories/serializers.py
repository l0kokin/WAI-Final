from rest_framework import serializers
from .models import CardContent, GraduateSuccess

class CardContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardContent
        fields = '__all__'

class GraduateSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduateSuccess
        fields = '__all__'
