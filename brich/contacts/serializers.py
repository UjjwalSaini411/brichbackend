from rest_framework import serializers
from .models import CallbackRequest, ContactUsRequest, CreatorsRequest, CreatorsCallbackRequest

class CallbackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackRequest
        fields = '__all__'
        
class CreatorsCallbackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorsCallbackRequest
        fields = '__all__'

class ContactUsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = '__all__'
        
class CreatorsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = '__all__'
