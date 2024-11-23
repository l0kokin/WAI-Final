from django.urls import path
from .views import CardContentList, GraduateSuccessList

urlpatterns = [
    path('api/card-content/', CardContentList.as_view(), name='card-content'),
    path('api/graduate-success/', GraduateSuccessList.as_view(),
         name='graduate-success'),
]
