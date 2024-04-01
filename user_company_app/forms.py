from django import forms
from django.contrib.auth.models import User
from .models import Company



'''Edit the Company model info form'''
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
        
'''Add the new manager to the company form'''    
class AddNewManagerForm(forms.Form):
    manager = forms.ModelChoiceField(queryset=User.objects.exclude(username='admin'),
                                     widget=forms.Select(attrs={'class': 'form-control',
                                                                'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                'onfocusout': 'this.style.borderColor="";'}))

'''Delete the managers from the company form'''
class DeleteManagerForm(forms.Form):
    
    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        if company:
            self.fields['delete_managers'].queryset = User.objects.filter(companies=company)

    delete_managers = forms.ModelChoiceField(queryset=User.objects.none(),
                                      widget=forms.Select(attrs={'class': 'form-control',
                                                                 'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                 'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                 'onfocusout': 'this.style.borderColor="";'}))
   
        
class CompanyLogoForm(forms.ModelForm):
    company_logo = forms.ImageField(label='Company Logo', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Company
        fields = ['company_logo']
        
class DeleteCompanyForm(forms.Form):
    delete_company_widget_form = {'class': 'form-control', 
                        'size': '30', 
                        'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                        'onfocus': 'this.style.borderColor="#019cbb";', 
                        'onfocusout': 'this.style.borderColor="";'
                    }
    company_email = forms.EmailField(label='Confirm Company Email', widget=forms.EmailInput(attrs=delete_company_widget_form))       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        