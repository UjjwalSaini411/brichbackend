from django.urls import path
from .views import CallbackRequestListCreateView, submit_callback_request, ContactUsRequestListCreateView, submit_contact_us_request, submit_creators_request, Creators_callback_request

urlpatterns = [
    path('callback-requests/', CallbackRequestListCreateView.as_view(), name='callback-request-list-create'),
    path('submit-callback-request/', submit_callback_request, name='submit-callback-request'),
    path('creators-callback-request/', Creators_callback_request, name='creators-callback-request'),
    path('contact-us/', submit_contact_us_request, name='contact-us-list-create'),
    path('creators/', submit_creators_request, name='creators-list-create'),  # Define the URL for CreatorsRequest view
]

