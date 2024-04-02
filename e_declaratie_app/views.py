from django.shortcuts import render


def home(request):
    '''Return the first page of e-declaration website'''
    return render(request, "e_declaratie_html_files/mainpage.html")