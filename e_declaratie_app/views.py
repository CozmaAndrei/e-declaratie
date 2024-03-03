from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_company_app.models import Company
from django.contrib import messages

'''Return the first page of e-declaration website'''
def home(request):
    return render(request, "e_declaratie_html_files/mainpage.html")