from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearchArticleViewSet

router = DefaultRouter()
router.register(r'research-articles', ResearchArticleViewSet,
                basename='research-article')

urlpatterns = [
    path('', include(router.urls)),
]
