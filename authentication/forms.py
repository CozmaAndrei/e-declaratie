from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from companies.models import Company

'''This form is used for user registration'''
class UserRegisterForm(UserCreationForm):
    #user_widget_register_form using for style in all collumns"
    user_widget_register_form = {'class': 'form-control', 
                                'size': '30', 
                                'style': 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);', 
                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                'onfocusout': 'this.style.borderColor="";'}
    
    first_name = forms.CharField(label="Nume", min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_register_form))
    last_name = forms.CharField(label="Prenume", min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_register_form))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs=user_widget_register_form))

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
        
        self.fields['username'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        self.fields['password1'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        self.fields['password2'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        
        self.fields['username'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['username'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['password1'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['password1'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['password2'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['password2'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'

'''THis form is used for custom Authentication(added style)'''
class CustomAuthenticationForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
        self.fields['username'].label = 'Utilizator'
        self.fields['password'].label = 'Parola'
        
        self.fields['username'].widget.attrs['size'] = '30'
        self.fields['password'].widget.attrs['size'] = '30'
        
        self.fields['username'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        self.fields['password'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        
        self.fields['username'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['username'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['password'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['password'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'

'''This form is used for company registration'''
class CompanyRegisterForm(forms.ModelForm):
    #register_widget_form using for style in all collumns"
    register_widget_form = {'class': 'form-control', 
                            'size': '30', 
                            'style': 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);', 
                            'onfocus': 'this.style.borderColor="#019cbb";', 
                            'onfocusout': 'this.style.borderColor="";'}
    
    company_name = forms.CharField(label ='Nume firma', min_length=3, max_length=50, widget=forms.TextInput(attrs=register_widget_form))
    company_email = forms.EmailField(label ='Email firma', widget=forms.EmailInput(attrs=register_widget_form))
    company_cui = forms.CharField(label ='CUI', min_length=3, max_length=50, widget=forms.TextInput(attrs=register_widget_form))
    company_register_number = forms.CharField(label ='Numar registru', min_length=3, max_length=50, widget=forms.TextInput(attrs=register_widget_form))
    company_address = forms.CharField(label='Adresa firma', min_length=3, max_length=50, widget=forms.TextInput(attrs=register_widget_form))
    company_city = forms.CharField(label='Oras', min_length=3, max_length=50, widget=forms.TextInput(attrs=register_widget_form))
    contact_person_phone = forms.CharField(label='Contact', required=False, widget=forms.TextInput(attrs=register_widget_form))    
    class Meta:
        model = Company
        fields = ['company_name', 'company_email', 'company_cui', 'company_register_number', 'company_address', 'company_city', 'contact_person_phone']

