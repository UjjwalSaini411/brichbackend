from rest_framework import generics
from .models import CallbackRequest, ContactUsRequest, CreatorsRequest , CreatorsCallbackRequest , CreatorsIND
from .serializers import CallbackRequestSerializer, ContactUsRequestSerializer, CreatorsRequestSerializer, CreatorsCallbackRequestSerializer , CreatorsINDRequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging
from django.core.mail import send_mail


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
    
class CreatorsINDRequestListCreateView(generics.ListCreateAPIView):
    queryset = CreatorsRequest.objects.all()
    serializer_class = CreatorsINDRequestSerializer
    

    
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


@api_view(['POST'])
def submit_CreatorsIND_request(request):
    print("in creators IND data",request.data)
    if request.method == 'POST':
        name = request.data.get('name')
        phone_number = request.data.get('mobile')
        email = request.data.get('email')
        socialLink = request.data.get('socialMediaLink')
        creatorType = request.data.get('creatorType')
        description = request.data.get('description')

        if (
            name and 
            phone_number and  
            email and socialLink and creatorType
            and description
        ):
            creators_request = CreatorsIND(
                name=name,  
                phone_number=phone_number,
                email=email,
                description=description,
                creatorType = creatorType,
                socialLink  = socialLink

            )
            creators_request.save()  
            subject = 'New CreatorsIND Form Submission'
            message = f'Name: {name}\nEmail: {email}\nCreator Type: {creatorType}\n Social Link: {socialLink}\n Description: {description}\n'  # Customize this with all form fields
            from_email = 'sainiujjwal411@gmail.com'
            recipient_list = ['ujjwalsaini411@gmail.com']  # Replace with your email address or a list of recipient addresses

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            logger.info(f"Saved CreatorsRequest: {creators_request}")
            return Response({'message': 'Creators request submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            logger.error('Invalid data')
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.warning('Invalid request method')
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)