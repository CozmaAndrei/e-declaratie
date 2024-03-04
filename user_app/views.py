from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from user_company_app.models import Company
from user_company_app.forms import EditCompanyInfoForm
from user_company_app.forms import AddNewManagerForm
from .forms import EditUserInfoForm
from .models import ExtraUserInformations



'''Return user profile with his username in URL and user information in profilepage.html'''
def user_profile(request, username): #used for profilepage.html
    username = request.user
    the_user_name = User.objects.get(username=username)
    extra_info = ExtraUserInformations.objects.get(user=the_user_name) #used to get informations from ExtraUserInformations model
    return render(request, 'user_html/profilepage.html', {"the_user_name": the_user_name, "extra_info": extra_info})

'''Update the user info, like username, first name, last name, etc'''
def update_user_info(request, username):
    user = User.objects.get(username=username)
    extra_info = ExtraUserInformations.objects.get(user=user)
    if request.method == "POST":
        form = EditUserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            extra_info.date_of_birth = form.cleaned_data['date_of_birth']
            extra_info.save()
            messages.success(request, "Your profile was edited with success!")
            return redirect ('user_profile', user.username)
    else:
        form = EditUserInfoForm(instance=user)
    return render(request, 'user_html/updateuserprofileinfo.html', { "form": form})

'''Delete the user account with conditions'''
def delete_user_account(request, user_id):
    user = User.objects.get(pk=user_id)
    user_companies = Company.objects.filter(managers=user)

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
    else:
        user.delete()
        messages.success(request, "Your account was deleted!")
    
    return redirect('register_user')

'''Return all the users without the current user and admin in userlistpage.html'''
def users_list(request):
    all_users = User.objects.exclude(username=request.user).exclude(username='admin') #used in userlistpage.html
    return render(request, 'user_html/userslistpage.html', {"all_users": all_users})

'''Return the user view profile in viewprofilepage.html for all the users'''
def user_view_profile(request, username):
    view_user = User.objects.get(username=username) #used in viewprofilepage.html
    extra_view_user_info = ExtraUserInformations.objects.get(user=view_user) #request in ExtraUserInformations model for table fields
    return render(request, 'user_html/viewprofilepage.html', {"view_user": view_user, "extra_view_user_info": extra_view_user_info})

def change_pass(request,username):
    return render(request, 'user_html/changeuserpass.html/', {})















































