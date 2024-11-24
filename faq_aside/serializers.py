from rest_framework import serializers
from .models import FaqAside


class FaqAsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAside
        fields = '__all__'
