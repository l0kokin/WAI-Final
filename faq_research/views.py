from rest_framework.viewsets import ModelViewSet
from .models import ResearchArticle
from .serializers import ResearchArticleSerializer


class ResearchArticleViewSet(ModelViewSet):
    queryset = ResearchArticle.objects.all()
    serializer_class = ResearchArticleSerializer
