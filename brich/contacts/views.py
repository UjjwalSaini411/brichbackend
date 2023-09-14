from rest_framework import generics
from .models import CallbackRequest, ContactUsRequest
from .serializers import CallbackRequestSerializer, ContactUsRequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CallbackRequestListCreateView(generics.ListCreateAPIView):
    queryset = CallbackRequest.objects.all()
    serializer_class = CallbackRequestSerializer

class ContactUsRequestListCreateView(generics.ListCreateAPIView):
    queryset = ContactUsRequest.objects.all()
    serializer_class = ContactUsRequestSerializer
    
@api_view(['POST'])
def submit_callback_request(request):
    if request.method == 'POST':
        full_name = request.data.get('full_name')
        phone_number = request.data.get('phone_number')

        if full_name and phone_number:
            callback_request = CallbackRequest(full_name=full_name, phone_number=phone_number)
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
def submit_contact_us_request(request):
    if request.method == 'POST':
        company_name = request.data.get('company_name')
        nature_of_business = request.data.get('nature_of_business')
        address = request.data.get('address')
        postcode = request.data.get('postcode')
        contact_name = request.data.get('contact_name')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        needs_description = request.data.get('needs_description')

        if (
            company_name and nature_of_business and address and
            postcode and contact_name and phone_number and
            email and needs_description
        ):
            contact_us_request = ContactUsRequest(
                company_name=company_name,
                nature_of_business=nature_of_business,
                address=address,
                postcode=postcode,
                contact_name=contact_name,
                phone_number=phone_number,
                email=email,
                needs_description=needs_description
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