from django import forms

class MyForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'myTextarea',
                                                        'class': 'form-control',
                                                        'rows': 6,
                                                        'cols': 2,
                                                        'style': 'padding: 10px;'
                                                        }))