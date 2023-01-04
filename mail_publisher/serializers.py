from rest_framework import serializers


class MailPublisherSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    to_email = serializers.EmailField()
    message = serializers.CharField()
    attachments = serializers.ListField(child=serializers.FileField(), required=False)
