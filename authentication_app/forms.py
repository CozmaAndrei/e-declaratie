from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Company

        
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, 
                                 max_length=50, 
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                                               'size': '30', 
                                                               'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                               'onfocus': 'this.style.borderColor="#019cbb";', 
                                                               'onfocusout': 'this.style.borderColor="";'}))
    last_name = forms.CharField(min_length=3, 
                                max_length=50, 
                                widget=forms.TextInput(attrs={'class': 'form-control', 
                                                              'size': '30', 
                                                              'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                              'onfocus': 'this.style.borderColor="#019cbb";', 
                                                              'onfocusout': 'this.style.borderColor="";'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 
                                                               'size': '30', 
                                                               'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                               'onfocus': 'this.style.borderColor="#019cbb";', 
                                                               'onfocusout': 'this.style.borderColor="";'}))
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
        self.fields['username'].widget.attrs['size'] = '30'
        self.fields['password1'].widget.attrs['size'] = '30'
        self.fields['password2'].widget.attrs['size'] = '30'
        
        self.fields['username'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['password1'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['password2'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        
        self.fields['username'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['username'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['password1'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['password1'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['password2'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['password2'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'


class CustomAuthenticationForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
        self.fields['username'].widget.attrs['size'] = '30'
        self.fields['password'].widget.attrs['size'] = '30'
        
        self.fields['username'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['password'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        
        self.fields['username'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['username'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['password'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['password'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'

class CompanyRegisterForm(forms.ModelForm):
    company_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))
    company_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))
    company_cui = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))
    company_register_number = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))
    company_address = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))
    company_city = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))
    contact_person_phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'size': '30', 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 'onfocus': 'this.style.borderColor="#019cbb";', 'onfocusout': 'this.style.borderColor="";'}))    
    class Meta:
        model = Company
        fields = ['company_name', 'company_email', 'company_cui', 'company_register_number', 'company_address', 'company_city', 'contact_person_phone']  
    
    def __init__(self, *args, **kwargs):
        super(CompanyRegisterForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].label = 'Company name'
        self.fields['company_email'].label = 'Company email'
        self.fields['company_cui'].label = 'Fiscal Identification Code'
        self.fields['company_register_number'].label = 'Registry Number'
        self.fields['company_address'].label = 'Company address'
        self.fields['company_city'].label = 'City'
        self.fields['contact_person_phone'].label = 'Contact phone'