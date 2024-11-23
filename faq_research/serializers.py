from rest_framework import serializers
from .models import ResearchArticle


class ResearchArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchArticle
        fields = ['id', 'title', 'url', 'author']
