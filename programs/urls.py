from django.urls import path
from .views import ProgramListView

urlpatterns = [
    path('programs/', ProgramListView.as_view(), name='program-list'),
]
