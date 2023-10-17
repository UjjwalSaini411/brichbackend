from rest_framework import generics
from .models import CallbackRequest, ContactUsRequest, CreatorsRequest , CreatorsCallbackRequest
from .serializers import CallbackRequestSerializer, ContactUsRequestSerializer, CreatorsRequestSerializer, CreatorsCallbackRequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger()

class CallbackRequestListCreateView(generics.ListCreateAPIView):
    queryset = CallbackRequest.objects.all()
    serializer_class = CallbackRequestSerializer
    
class CreatorsCallbackRequestListCreateView(generics.ListCreateAPIView):
    queryset = CreatorsCallbackRequest.objects.all()
    serializer_class = CreatorsCallbackRequestSerializer

class ContactUsRequestListCreateView(generics.ListCreateAPIView):
    queryset = ContactUsRequest.objects.all()
    serializer_class = ContactUsRequestSerializer

class CreatorsRequestListCreateView(generics.ListCreateAPIView):
    queryset = CreatorsRequest.objects.all()
    serializer_class = CreatorsRequestSerializer
    

    
@api_view(['POST'])
def submit_callback_request(request):
    print("homepage callback req data is", request.data)
    if request.method == 'POST':
        full_name = request.data.get('name')
        phone_number = request.data.get('number')
        send_from = request.data.get('where')


        if full_name and phone_number:
            callback_request = CallbackRequest(full_name=full_name, phone_number=phone_number, send_from=send_from)
            callback_request.save()
            logger.info(f"Saved CallbackRequest: {callback_request}")
            return Response({'message': 'Callback request submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            logger.error('Invalid data')
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.warning('Invalid request method')
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
@api_view(['POST'])
def Creators_callback_request(request):
    print("creator callback", request.data)
    if request.method == 'POST':
        full_name = request.data.get('name')
        phone_number = request.data.get('number')
        send_from = request.data.get('where')

        if full_name and phone_number:
            callback_request = CreatorsCallbackRequest(full_name=full_name, phone_number=phone_number, send_from=send_from)
            callback_request.save()
            logger.info(f"Saved CreatorsCallbackRequest: {callback_request}")
            return Response({'message': 'Callback request submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            logger.error('Invalid data')
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.warning('Invalid request method')
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





@api_view(['POST'])
def submit_contact_us_request(request):
    print(request.data)
    if request.method == 'POST':
        company_name = request.data.get('company_name')
        nature_of_business = request.data.get('nature_of_business')
        address = request.data.get('address')
        postcode = request.data.get('postcode')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        send_from = request.data.get('send_from')

        if (
            company_name and nature_of_business and address and
            postcode and phone_number and
            email 
        ):
            contact_us_request = ContactUsRequest(
                company_name=company_name,
                nature_of_business=nature_of_business,
                address=address,
                postcode=postcode,
                phone_number=phone_number,
                email=email,
                send_from=send_from,
            )
            contact_us_request.save()
            logger.info(f"Saved ContactUsRequest: {contact_us_request}")
            return Response({'message': 'Contact Us request submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            logger.error('Invalid data')
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.warning('Invalid request method')
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['POST'])
def submit_creators_request(request):
    print("in creators data",request.data)
    if request.method == 'POST':
        name = request.data.get('name')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        send_from = request.data.get('send_from')
        needs_description = request.data.get('needs_description')

        if (
            name and 
            phone_number and  
            email 
        ):
            creators_request = CreatorsRequest(
                name=name,  
                phone_number=phone_number,
                email=email,
                needs_description=needs_description,
                send_from=send_from,

            )
            creators_request.save()  
            logger.info(f"Saved CreatorsRequest: {creators_request}")
            return Response({'message': 'Creators request submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            logger.error('Invalid data')
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.warning('Invalid request method')
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
