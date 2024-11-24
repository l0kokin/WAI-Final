from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FaqAside
from .serializers import FaqAsideSerializer


class FaqAsideListView(APIView):
    def get(self, request):
        faq_aside_items = FaqAside.objects.all()
        serializer = FaqAsideSerializer(faq_aside_items, many=True)
        return Response(serializer.data)
