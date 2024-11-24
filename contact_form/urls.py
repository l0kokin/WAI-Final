from django.urls import path

from contact_form.views import ContactFormView

urlpatterns=[
    path('', ContactFormView.as_view(), name='contact-form'),
]