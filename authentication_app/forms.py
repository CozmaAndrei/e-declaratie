from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from user_company_app.models import Company
from datetime import datetime


class UserRegisterForm(UserCreationForm):
    
    user_widget_register_form = {'class': 'form-control', 
                                'size': '30', 
                                'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                'onfocusout': 'this.style.borderColor="";'}
    
    first_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_register_form))
    last_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_register_form))
    email = forms.EmailField(widget=forms.EmailInput(attrs=user_widget_register_form))
    date_of_birth= forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(datetime.now().year, 1900, -1),
                                                                                       attrs={'class': 'form-select',
                                                                                            'size': '1',
                                                                                            'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                                            'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                                            'onfocusout': 'this.style.borderColor="";'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2']
        
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
    
    '''We check if the user have at least 18 years'''  
    def clean_date_of_birth(self):
        birth_date = self.cleaned_data["date_of_birth"]
        actual_date = datetime.now().date()
        dif = actual_date - birth_date
        age = dif.days // 365
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to create an account.")
        
        return birth_date

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
    #register_widget_form using for style in all collumns"
    register_widget_form = {'class': 'form-control', 
                            'size': '30', 
                            'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                            'onfocus': 'this.style.borderColor="#019cbb";', 
                            'onfocusout': 'this.style.borderColor="";'}
    
    company_name = forms.CharField(min_length=3, max_length=50, label ='Company name', widget=forms.TextInput(attrs=register_widget_form))
    company_email = forms.EmailField(label ='Company email', widget=forms.EmailInput(attrs=register_widget_form))
    company_cui = forms.CharField(min_length=3, max_length=50, label ='Fiscal Identification Code', widget=forms.TextInput(attrs=register_widget_form))
    company_register_number = forms.CharField(min_length=3, max_length=50, label ='Registry Number', widget=forms.TextInput(attrs=register_widget_form))
    company_address = forms.CharField(min_length=3, max_length=50, label='Company address', widget=forms.TextInput(attrs=register_widget_form))
    company_city = forms.CharField(min_length=3, max_length=50, label='City', widget=forms.TextInput(attrs=register_widget_form))
    contact_person_phone = forms.CharField(required=False, label='Contact phone', widget=forms.TextInput(attrs=register_widget_form))    
    class Meta:
        model = Company
        fields = ['company_name', 'company_email', 'company_cui', 'company_register_number', 'company_address', 'company_city', 'contact_person_phone']