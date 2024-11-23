from rest_framework import serializers
from .models import LiteracyCard


class LiteracyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiteracyCard
        fields = '__all__'
