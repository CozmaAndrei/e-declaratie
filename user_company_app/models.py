import os
from django.db import models
from django.contrib.auth.models import User



def company_directory_path(instance, filename):
    '''This function is used to create a new folder for each company and save his logo in it. 
        The folder name is the company's name.
        The function are used in the Company model in the company_logo field.'''
    new_name_of_folder = f"{instance.company_name}'s_logo"
    filename = instance.company_name + '.png'
    return os.path.join('company_logo', new_name_of_folder + '/' + filename)

class Company(models.Model):
    '''This model is used to store informations about the company, like his name, logo, email, etc.'''
    managers = models.ManyToManyField(User, related_name='companies', blank=True) # the user that is associated with the company
    company_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100, unique=True)
    company_cui = models.CharField(max_length=50, unique=True)
    company_register_number = models.CharField(max_length=50, unique=True)
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=50)
    contact_person_phone = models.CharField(max_length=25, blank=True, null=False)
    company_logo = models.ImageField(upload_to=company_directory_path, blank=True, null=True)
    
    class Meta:
        db_table = 'Companies'
        
    def __str__(self):
        return self.company_name #plus many fields if you want
