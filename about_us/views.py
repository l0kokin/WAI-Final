# programs/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsView(APIView):
    def get(self, request):
        aboutUs = AboutUs.objects.all()
        serializer = AboutUsSerializer(aboutUs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
