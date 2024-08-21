from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.views.decorators.cache import never_cache

@never_cache
def home(request):
    '''Return the first page of e-declaration website'''
    return render(request, "e_declaratie_html_files/index.html")