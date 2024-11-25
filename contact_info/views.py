from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import ContactInfo
from .serializers import ContactInfoSerializer

class ContactInfoView(RetrieveAPIView):
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.latest('id')