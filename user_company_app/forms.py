from django import forms
from django.contrib.auth.models import User
from authentication_app.models import Company

'''The company profile editing form'''
class EditCompanyInfoForm(forms.ModelForm):
    company_name = forms.CharField(min_length=3, max_length=50, 
                                   widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                 'size': '30', 
                                                                 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                 'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                 'onfocusout': 'this.style.borderColor="";'}))
    company_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 
                                                                    'size': '30', 
                                                                    'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                    'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                    'onfocusout': 'this.style.borderColor="";'}))
    company_cui = forms.CharField(min_length=3, max_length=50, 
                                  widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                'size': '30', 
                                                                'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                'onfocusout': 'this.style.borderColor="";'}))
    company_register_number = forms.CharField(min_length=3, max_length=50, 
                                              widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                            'size': '30', 
                                                                            'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                            'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                            'onfocusout': 'this.style.borderColor="";'}))
    company_address = forms.CharField(min_length=3, max_length=50, 
                                      widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                    'size': '30', 
                                                                    'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                    'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                    'onfocusout': 'this.style.borderColor="";'}))
    company_city = forms.CharField(min_length=3, max_length=50, 
                                   widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                 'size': '30', 
                                                                 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                 'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                 'onfocusout': 'this.style.borderColor="";'}))
    contact_person_phone = forms.CharField(required=False, 
                                           widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                         'size': '30', 
                                                                         'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                         'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                         'onfocusout': 'this.style.borderColor="";'}))
    class Meta:
        model = Company
        fields = ['company_name', 'company_email', 'company_cui', 'company_register_number', 'company_address', 'company_city', 'contact_person_phone']
        
'''The new manager adding form'''    
class AddNewManagerForm(forms.Form):
    manager = forms.ModelChoiceField(queryset=User.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control', 
                                                                'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                'onfocusout': 'this.style.borderColor="";'}))      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        