from django import forms
from django.contrib.auth.models import User
from user_company_app.models import Company
from datetime import datetime
        

'''The user profile editing form'''
class EditUserInfoForm(forms.ModelForm):
    #user_widget_form using to style some of the fields"
    user_widget_form = {'class': 'form-control', 
                        'size': '30', 
                        'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                        'onfocus': 'this.style.borderColor="#019cbb";', 
                        'onfocusout': 'this.style.borderColor="";'}
    
    username = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_form))
    first_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_form))
    last_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_form))
    email = forms.EmailField(widget=forms.EmailInput(attrs=user_widget_form))
    
    # date_of_birth= forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(datetime.now().year, 1900, -1),
    #                                                                                    attrs={'class': 'form-select',
    #                                                                                         'size': '1',
    #                                                                                         'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
    #                                                                                         'onfocus': 'this.style.borderColor="#019cbb";', 
    #                                                                                         'onfocusout': 'this.style.borderColor="";'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']