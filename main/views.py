from django.shortcuts import render
from django.utils.translation import gettext as _

def home(request):
    '''Return the first page of e-declaration website'''
    return render(request, "e_declaratie_html_files/index.html")