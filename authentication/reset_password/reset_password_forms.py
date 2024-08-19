from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


'''This form is used to apply style for Custom Reset Pass'''
class CustomResetPasswordForm(PasswordResetForm):
    # clasa copil CustomResetPasswordForm extinde clasa parinte PasswordResetForm
    def __init__(self, *args, **kwargs):
        # __init__ este constructorul clasei si se apeleaza automat cand se creaza o instanta
        # *args > o conventie in py pentru a reprezenta un numar de argumente de tip tuplu in functie (da-i exemplu cu suma)
        # ** kwargs > o conventie in py pentru a reprezenta un numar de argumente de tip dictionar in functie.
        # De ce am folosit *args si **kwargs? > ma asigur ca toate argumentele posibile sunt transmise corect catre clasa parinte
        # De ce am folosit self? > este un parametru special folosit pentru a se referi la instanța curentă a clasei.
        super().__init__(*args, **kwargs)
        # super() este apelul constructorului clasei parinte
        # super() > Acest apel asigură că toate inițializările și setările din PasswordResetForm sunt efectuate înainte de a adăuga modificările specifice clasei copil.
        # super() > Fără acest apel, inițializarea clasei părinte ar fi omisă, ceea ce ar putea duce la erori.
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