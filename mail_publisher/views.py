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
        data = request.data
        files = request.FILES.getlist("attachments")
        attachments = {}

        for file in files:
            attachments[file.name] = ContentFile(file.read())

        incoming_mails = data["to_email"]
        mail_type = type(incoming_mails)
        
        
        if mail_type is str:
            incoming_mails = [incoming_mails]
        
        
        if mail_type not in (list, str):
            return Response({"to_email": "Should be a string or a list of emails"}, status=status.HTTP_400_BAD_REQUEST)

        data["to_email"] = incoming_mails
        serializer = MailPublisherSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        for incoming_mail in incoming_mails:
            mail.send(
            incoming_mail,
            FROM_EMAIL,
            subject=serializer.data.get("subject"),
            html_message=serializer.data.get("message"),
            cc=serializer.data.get("cc"),
            bcc=serializer.data.get("bcc"),
            attachments=attachments,
        )

        return Response(None, status=status.HTTP_204_NO_CONTENT)
