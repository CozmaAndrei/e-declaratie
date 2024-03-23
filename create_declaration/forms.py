from django import forms

class MyForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 100, 'style': 'resize:none; padding: 10px;'}))

