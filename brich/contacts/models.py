from django.db import models

class CallbackRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    send_from = models.CharField(max_length=255, default='homepage') 


    def __str__(self):
        return self.full_name
    

class CreatorsCallbackRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    send_from = models.CharField(max_length=255, default='homepage')

    def __str__(self):
        return self.full_name

    


class ContactUsRequest(models.Model):
    company_name = models.CharField(max_length=255)
    nature_of_business = models.CharField(max_length=255)
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    send_from = models.CharField(max_length=255, default='homepage') 

    

    def __str__(self):
        return self.company_name
    
    
class CreatorsRequest(models.Model):

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    needs_description = models.TextField()
    send_from = models.CharField(max_length=255, default='homepage') 

    

    def __str__(self):
        return self.name


class CreatorsIND(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    creatorType = models.CharField(max_length=255)
    socialLink = models.CharField(max_length=255)
    description = models.TextField()

    

    def __str__(self):
        return self.name