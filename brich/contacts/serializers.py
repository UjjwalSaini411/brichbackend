from rest_framework import serializers
from .models import CallbackRequest, ContactUsRequest

class CallbackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackRequest
        fields = '__all__'

class ContactUsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = '__all__'
