from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from post_office import mail
from rest_framework import permissions
from rest_framework import status
from .serializers import MailPublisherSerializer
from core.settings import FROM_EMAIL
from django.core.files.base import ContentFile


class MailPublisher(APIView):
    """Publishes emails sent via request body

    Args:
        request: Django Request object

    Returns:
        Response: Django rest framework response
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = MailPublisherSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        files = request.FILES.getlist("attachments")
        attachments = {}

        for file in files:
            attachments[file.name] = ContentFile(file.read())

        mail.send(
            serializer.data.get("to_email"),
            FROM_EMAIL,
            subject=serializer.data.get("subject"),
            html_message=serializer.data.get("message"),
            attachments=attachments,
        )

        return Response(None, status=status.HTTP_204_NO_CONTENT)
