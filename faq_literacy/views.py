from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LiteracyCard
from .serializers import LiteracyCardSerializer


class LiteracyCardList(APIView):
    def get(self, request):
        literacy_cards = LiteracyCard.objects.all()
        serializer = LiteracyCardSerializer(literacy_cards, many=True)
        return Response(serializer.data)
