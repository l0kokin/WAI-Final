# programs/serializers.py
from rest_framework import serializers
from .models import Program

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'title', 'description', 'image_url', 'color']
