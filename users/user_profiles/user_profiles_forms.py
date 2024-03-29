from django import forms

class ReportForm(forms.Form):
    '''The report form using the Form class from the forms module.'''
    
    reason = forms.ChoiceField(label="Choices the reason for reporting", choices=[
                                                                                ('Inappropriate Profile Image', 'Inappropriate Profile Image'),
                                                                                ('Inappropriate User Name', 'Inappropriate User Name'),
                                                                                ('Inappropriate User Information', 'Inappropriate User Information'),
                                                                                ('Other', 'Other (Please specify in the description box below)')
                                                                            ], widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Please provide a detailed description of the issue'}))