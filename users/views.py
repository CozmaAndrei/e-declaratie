from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from companies.models import Company
from .forms import EditUserInfoForm, ChangeUserPassForm, UserPicForm, DeleteUserForm
from .models import ExtraUserInformations
from django.contrib.auth import login, logout

from django.http import Http404

def user_profile(request, username): #used for userprofile.html
    '''Return the user profile with his username in URL and user information in userprofile.html'''
    try:
        the_user_name = User.objects.get(username=username)
        extra_info = ExtraUserInformations.objects.get(user=the_user_name) #used to get informations from ExtraUserInformations model
    except User.DoesNotExist:
        raise Http404("User does not exist") #used to get informations from ExtraUserInformations model
    
    context = {
        "the_user_name": the_user_name,
        "extra_info": extra_info
    }
    return render(request, 'user_html/userprofile.html', context)

def update_user_info(request, username):
    '''Update the user info like username, first name, last name, etc with conditions and return the user profile in updateuserprofileinfo.html'''
    user = User.objects.get(username=username)
    extra_info = ExtraUserInformations.objects.get(user=user)
    if request.method == "POST":
        form = EditUserInfoForm(request.POST, instance=user)
        user_pic_form = UserPicForm(request.POST, request.FILES, instance=extra_info)
        if form.is_valid() and user_pic_form.is_valid():
            if form.cleaned_data['username'] != request.user.username:
                form.save()
                extra_info.date_of_birth = form.cleaned_data['date_of_birth']
                extra_info.save()
                user_pic_form.save()
                user.save()
                logout(request)
                return redirect ('login_user')
            else:
                form.save()
                extra_info.date_of_birth = form.cleaned_data['date_of_birth']
                extra_info.save()
                user_pic_form.save()
                user.save()
                messages.success(request, "Your profile was edited with success!")
                return redirect ('user_profile', user.username)
    else:
        form = EditUserInfoForm(instance=user)
        user_pic_form = UserPicForm(instance=extra_info)
        
    context = {
        "form": form,
        "user_pic_form": user_pic_form,
        "user": user,
        "extra_info": extra_info
    }
    return render(request, 'user_html/updateuserprofileinfo.html', context)

def delete_user_account(request, user_id):
    '''Delete the user account with conditions and return the register_user.html page after the user account was deleted'''
    user = User.objects.get(pk=user_id)
    user_companies = Company.objects.filter(managers=user)
    
    if request.method == "POST":
        delete_form = DeleteUserForm(request.POST or None)
        if delete_form.is_valid():
            email = delete_form.cleaned_data['email']
            if request.user.email == email:
                user = User.objects.get(email=email)
                if user_companies: #if user has a company
                    for company in user_companies:
                        managers = company.managers.all()
                        if len(managers) == 1 and user in managers: #if the user is the only one manager on his company, then he must delete the company first
                            if company.managers.count() == 1:
                                messages.warning(request, "You must delete the company account first!")
                                return redirect('user_profile', request.user.username)
                        elif len(managers) > 1 and user in managers: #if the company has many managers, then the user can delete the account
                            user.delete()
                            messages.success(request, "Your account was deleted!")
                            return redirect('register_user')
                else: #if user has no company
                    user.delete()
                    messages.success(request, "Your account was deleted!")
            else:
                messages.error(request, "The email you entered is not your email")
                return redirect('delete_user_account', user_id)
    else:
        delete_form = DeleteUserForm()  
     
    return render(request, "user_html/deleteuseraccount.html", {"delete_form": delete_form, "user": user, "user_companies": user_companies})

def change_pass(request,username):
    '''Change the user password and return to the login page after the password was changed with success!'''
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ChangeUserPassForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been updated, Please log in again!")
            logout(request)
            return redirect('login_user')
    else:
        form = ChangeUserPassForm(request.user)   
    
    context = {
        "user": user,
        "form": form
    }      
    return render(request, 'user_html/changeuserpass.html', context)











