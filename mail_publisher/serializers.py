from rest_framework import serializers


class MailPublisherSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    to_email = serializers.ListField(child=serializers.EmailField())
    message = serializers.CharField()
    attachments = serializers.ListField(child=serializers.FileField(), required=False)
    cc = serializers.ListField(child=serializers.CharField(), required=False)
    bcc = serializers.ListField(child=serializers.CharField(), required=False)
