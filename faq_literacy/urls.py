from django.urls import path
from .views import LiteracyCardList

urlpatterns = [
    path('literacy-cards/', LiteracyCardList.as_view(), name='literacy-cards'),
]
