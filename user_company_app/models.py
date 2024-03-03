from django.db import models
from django.contrib.auth.models import User
    
'''Table for company registration'''
class Company(models.Model):
    managers = models.ManyToManyField(User, related_name='companies', blank=True) # the user that is associated with the company
    company_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100, unique=True)
    company_cui = models.CharField(max_length=50, unique=True)
    company_register_number = models.CharField(max_length=50, unique=True)
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=50)
    contact_person_phone = models.CharField(max_length=25, blank=True, null=False)
    
    class Meta:
        db_table = 'Companies'
        
    def __str__(self):
        return self.company_name #plus many fields if you want
