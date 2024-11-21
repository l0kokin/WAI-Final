from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CardContent, GraduateSuccess
from .serializers import CardContentSerializer, GraduateSuccessSerializer

class CardContentList(APIView):
    def get(self, request):
        cards = CardContent.objects.all()
        serializer = CardContentSerializer(cards, many=True)
        return Response(serializer.data)

class GraduateSuccessList(APIView):
    def get(self, request):
        graduates = GraduateSuccess.objects.all()
        serializer = GraduateSuccessSerializer(graduates, many=True)
        return Response(serializer.data)
