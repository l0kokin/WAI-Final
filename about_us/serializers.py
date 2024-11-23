# programs/serializers.py
from rest_framework import serializers
from .models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description']
