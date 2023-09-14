from django.db import models

class CallbackRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
    


class ContactUsRequest(models.Model):
    company_name = models.CharField(max_length=255)
    nature_of_business = models.CharField(max_length=255)
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    contact_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    needs_description = models.TextField()

    def __str__(self):
        return self.company_name
