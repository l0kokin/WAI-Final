from django.urls import path
from contact_info.views import ContactInfoCreateView

urlpatterns = [
    path('contact-info/', ContactInfoCreateView.as_view(), name='contact-info'),
]