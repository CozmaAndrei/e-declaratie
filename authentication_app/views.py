from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .forms import CustomAuthenticationForm
from .forms import CompanyRegisterForm
from user_company_app.models import Company
from users.models import ExtraUserInformations

'''Login function'''
def login_user(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect ('user_profile', username=username)
    
    else: 
        form = CustomAuthenticationForm()
    return render(request, 'auth_html_files/login_user.html', {'form': form}) 
    
'''Logout function'''
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('login_user') 

'''Register user function'''
def register_user(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            user = form.save(commit=False)
            user.save()
            date_of_birth = form.cleaned_data['date_of_birth']
            ExtraUserInformations.objects.create(user=user,date_of_birth=date_of_birth)
            messages.info(request, "Your user account was created, please Login!")
            return redirect('login_user')
    else:
        form = UserRegisterForm()
    return render(request, 'auth_html_files/register_user.html', {'form': form})
        
'''Company registration function'''
def register_company(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            company = form.save()
            company.managers.add(request.user)
            company.save()
            extra_info, created = ExtraUserInformations.objects.get_or_create(user=request.user)
            extra_info.user_company.add(company)
            logout(request)
            messages.success(request, "Your company account was created, please Login!")
            return redirect('login_user')
    else:
        form = CompanyRegisterForm()
    return render(request, 'auth_html_files/register_company.html', {'form': form})
    