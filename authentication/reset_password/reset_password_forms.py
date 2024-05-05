from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


'''This form is used to apply style for Custom Reset Pass'''
class CustomResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['size'] = '30'
        self.fields['email'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        self.fields['email'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['email'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
    
'''This form is used to apply style for Custom Set New Pass'''     
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['size'] = '30'
        self.fields['new_password2'].widget.attrs['size'] = '30'
        self.fields['new_password1'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        self.fields['new_password2'].widget.attrs['style'] = 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);'
        self.fields['new_password1'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['new_password1'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['new_password2'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['new_password2'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['new_password1'].help_text = None  