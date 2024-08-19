from django import forms

class ReportUserForm(forms.Form):
    '''The report form using the Form class from the forms module.'''
    
    reason = forms.ChoiceField(label="Motivul raportului", choices=[
                                                                    ('Imagine de profil neadecvată', 'Imagine de profil neadecvată'),
                                                                    ('Nume de utilizator inadecvat', 'Nume de utilizator inadecvat'),
                                                                    ('Informații inadecvate despre utilizator', 'Informații inadecvate despre utilizator'),
                                                                    ('Alt motiv', 'Alt motiv (Vă rugăm să specificați în caseta de descriere de mai jos)')
                                                                ], widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Descrierea raportului", 
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Vă rugăm să furnizați o descriere detaliată a problemei'}))