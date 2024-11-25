from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import logging
from .serializers import ContactMessageSerializer

logger = logging.getLogger(__name__)

class ContactFormView(APIView):
    def post(self, request):
        try:
            serializer = ContactMessageSerializer(data=request.data)
            if serializer.is_valid():
                logger.info(f"Attempting to send email from {serializer.validated_data['email']}")

                try:
                    # Print debugging information
                    print("Email settings:", {
                        "host": settings.EMAIL_HOST,
                        "port": settings.EMAIL_PORT,
                        "use_tls": settings.EMAIL_USE_TLS,
                        "user": settings.EMAIL_HOST_USER,
                        "has_password": bool(settings.EMAIL_HOST_PASSWORD),
                    })

                    send_mail(
                        subject=f"New message from {serializer.validated_data['name']}",
                        message=f"Message from {serializer.validated_data['name']} ({serializer.validated_data['email']}):\n\n{serializer.validated_data['message']}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.CONTACT_EMAIL],
                        fail_silently=False,
                    )

                    logger.info("Email sent successfully")
                    return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)

                except Exception as e:
                    logger.error(f"Failed to send email: {str(e)}")
                    return Response(
                        {"error": f"Failed to send email: {str(e)}"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
