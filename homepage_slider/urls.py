from django.urls import path
from .views import SliderAPIView


urlpatterns = [
    path('api/sliders/', SliderAPIView.as_view(), name='slider-api'),
]
