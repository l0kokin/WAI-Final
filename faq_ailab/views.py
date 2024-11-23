from rest_framework.viewsets import ModelViewSet
from .models import FaqAilab
from .serializers import FaqAilabSerializer


class FaqAilabViewSet(ModelViewSet):
    queryset = FaqAilab.objects.all()
    serializer_class = FaqAilabSerializer
