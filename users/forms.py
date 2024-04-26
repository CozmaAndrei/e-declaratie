from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from .models import ExtraUserInformations
from django.contrib.auth.forms import PasswordChangeForm
        

class EditUserInfoForm(forms.ModelForm):
    '''The user profile editing form'''
    user_widget_form = {'class': 'form-control', 
                        'size': '30', 
                        'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                        'onfocus': 'this.style.borderColor="#019cbb";', 
                        'onfocusout': 'this.style.borderColor="";'
                    }
    
    first_name = forms.CharField(min_length=3, max_length=50, label="Nume", widget=forms.TextInput(attrs=user_widget_form))
    last_name = forms.CharField(min_length=3, max_length=50, label="Prenume", widget=forms.TextInput(attrs=user_widget_form))
    email = forms.EmailField(widget=forms.EmailInput(attrs=user_widget_form))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ChangeUserPassForm(PasswordChangeForm):
    '''The change password form using the PasswordChangeForm imported from django.contrib.auth.forms'''
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    
    #applied Bootstrap
    def __init__(self, *args, **kwargs):
        '''We use the __init__ method to apply the Bootstrap classes to the fields and remove the help_text. 
            We also set the size and box-shadow for the fields and the onfocus and onfocusout events.'''
            
        super(ChangeUserPassForm, self).__init__(*args, **kwargs)
        
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        
        self.fields['old_password'].label = "Parola veche"
        self.fields['new_password1'].label = "Parola noua"
        self.fields['new_password2'].label = "Confirmare parola noua"
        
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        
        self.fields['old_password'].widget.attrs['size'] = '30'
        self.fields['new_password1'].widget.attrs['size'] = '30'
        self.fields['new_password2'].widget.attrs['size'] = '30'
        
        self.fields['old_password'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['new_password1'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['new_password2'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        
        self.fields['old_password'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['old_password'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['new_password1'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['new_password1'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['new_password2'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['new_password2'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
    
class UserPicForm(forms.ModelForm):
    '''The user profile picture form using the ImageField from the forms module. 
        We use the FileInput widget to style the field.'''  
        
    user_pic = forms.ImageField(label='Poza profil', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
         model = ExtraUserInformations
         fields = ['user_pic']
    
class DeleteUserForm(forms.Form):
    '''The form used to delete a user account. We use the EmailField to confirm the user's email.'''
    delete_user_widget_form = {'class': 'form-control', 
                        'size': '30', 
                        'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                        'onfocus': 'this.style.borderColor="#019cbb";', 
                        'onfocusout': 'this.style.borderColor="";'
                    }
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=delete_user_widget_form))


                                     




   