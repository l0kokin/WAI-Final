from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage
from .serializers import ContactMessageSerializer
import logging

logger = logging.getLogger(__name__)

class ContactFormView(APIView):
    def post(self, request):
        try:
            serializer = ContactMessageSerializer(data=request.data)
            if serializer.is_valid():
                # Save the message to the database
                contact_message = ContactMessage.objects.create(
                    name=serializer.validated_data['name'],
                    email=serializer.validated_data['email'],
                    message=serializer.validated_data['message']
                )
                logger.info(f"Saved contact message from {contact_message.email}")

                return Response({"message": "Message saved successfully!"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
