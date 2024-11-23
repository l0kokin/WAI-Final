from django.urls import path
from .views import AboutUsView


urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about-us'),
]
