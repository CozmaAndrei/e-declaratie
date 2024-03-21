from django.db import models
from django.db import models
from user_company_app.models import Company
import os


def company_stamp_path(instance, filename):
    '''This function is used to create a new folder for each company and save its company stamp in it.'''
    company_name = instance.extend_company_info.company_name
    filename = company_name + '.png'
    return os.path.join('company_stamps', company_name + '/' + filename)

def pdf_declaration_path(instance, filename):
    '''This function is used to create a new folder for each company and save its pdf declaration in it.'''
    company_name = instance.extend_company_info.company_name
    filename = company_name + '.pdf'
    return os.path.join('pdf_declarations', company_name + '/' + filename)

class ExtendCompanyModel(models.Model):
    '''This model is used to extend the Company model'''
    extend_company_info = models.OneToOneField(Company, on_delete=models.CASCADE)
    declaration_content = models.TextField(blank=True, null=True)
    company_stamp = models.ImageField(upload_to=company_stamp_path, blank=True, null=True)
    pdf_declaration = models.FileField(upload_to=pdf_declaration_path, blank=True, null=True)
    
    def __str__(self):
        return self.extend_company_info.company_name
