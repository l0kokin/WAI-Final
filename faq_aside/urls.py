from django.urls import path
from .views import FaqAsideListView

urlpatterns = [
    path('api/faq-aside/', FaqAsideListView.as_view(), name='faq-aside-list'),
]
