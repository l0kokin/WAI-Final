from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangoProject_final.models import Program
from programs.serializers import ProgramSerializer

class ProgramListView(APIView):
    def get(self, request):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
