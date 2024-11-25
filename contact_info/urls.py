from django.urls import path
from contact_info.views import ContactInfoView

urlpatterns = [
    path('', ContactInfoView.as_view(), name='contact-info'),
]