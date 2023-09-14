from django.urls import path
from .views import CallbackRequestListCreateView, submit_callback_request, ContactUsRequestListCreateView, submit_contact_us_request

urlpatterns = [
    path('callback-requests/', CallbackRequestListCreateView.as_view(), name='callback-request-list-create'),
    path('submit-callback-request/', submit_callback_request, name='submit-callback-request'),
    path('contact-us/', submit_contact_us_request, name='contact-us-list-create'),
]

