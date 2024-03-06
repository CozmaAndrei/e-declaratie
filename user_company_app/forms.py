from django import forms
from django.contrib.auth.models import User
from .models import Company

'''The company profile editing form'''
class EditCompanyInfoForm(forms.ModelForm):
    #company_widget_form style all the fields
    company_widget_form = {'class': 'form-control', 
                            'size': '30', 
                            'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                            'onfocus': 'this.style.borderColor="#019cbb";', 
                            'onfocusout': 'this.style.borderColor="";'}
    
    company_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=company_widget_form))
    company_email = forms.EmailField(widget=forms.EmailInput(attrs=company_widget_form))
    company_cui = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=company_widget_form))
    company_register_number = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=company_widget_form))
    company_address = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=company_widget_form))
    company_city = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=company_widget_form))
    contact_person_phone = forms.CharField(required=False, widget=forms.TextInput(attrs=company_widget_form))
    class Meta:
        model = Company
        fields = ['company_name', 'company_email', 'company_cui', 'company_register_number', 'company_address', 'company_city', 'contact_person_phone']
        
'''The new manager adding form'''    
class AddNewManagerForm(forms.Form):
    manager = forms.ModelChoiceField(queryset=User.objects.exclude(username='admin'),
                                     widget=forms.Select(attrs={'class': 'form-control',
                                                                'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                'onfocusout': 'this.style.borderColor="";'}))


class DeleteManagerForm(forms.Form):
    delete_manager = forms.ModelChoiceField(queryset=User.objects.exclude(username="admin"),
                                            widget=forms.Select(attrs={'class': 'form-control',
                                                                'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                'onfocusout': 'this.style.borderColor="";'}))        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        