from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import ContactInfo
from .serializers import ContactInfoSerializer

class ContactInfoCreateView(CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
