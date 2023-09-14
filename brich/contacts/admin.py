from django.contrib import admin
from .models import CallbackRequest
from .models import ContactUsRequest

admin.site.register(CallbackRequest)
admin.site.register(ContactUsRequest)
