from django.contrib import admin
from .models import CallbackRequest
from .models import ContactUsRequest
from .models import CreatorsRequest, CreatorsCallbackRequest, CreatorsIND

admin.site.register(CallbackRequest)
admin.site.register(ContactUsRequest)
admin.site.register(CreatorsRequest)
admin.site.register(CreatorsCallbackRequest)
admin.site.register(CreatorsIND)
