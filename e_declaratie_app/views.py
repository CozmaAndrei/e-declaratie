from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from authentication_app.models import Company
from .forms import EditUserInfoForm
from .forms import EditCompanyInfoForm
from .forms import AddNewManagerForm
from django.contrib import messages

'''Return the first page of e-declaration website'''
def home(request):
    return render(request, "e_declaratie_html_files/mainpage.html")

'''Return user profile with his username in URL and user information in profilepage.html'''
def user_profile(request, username):
    username = request.user
    the_user_name = User.objects.get(username=username) #used for profilepage.html
    return render(request, 'e_declaratie_html_files/profilepage.html', {"the_user_name": the_user_name})

'''Return all users asociated to company in companypage.html and the company name in URL '''
def company_profile(request, company_name):
    get_company_name = Company.objects.get(company_name=company_name) #used for companypage.html
    return render(request, 'e_declaratie_html_files/companypage.html', {"get_company_name": get_company_name})

'''Return all the companies without the current user company in companieslistpage.html'''
def companies_list(request):
    all_companies = Company.objects.exclude(managers=request.user) #used in for loop in companieslistpage.html
    return render(request, 'e_declaratie_html_files/companieslistpage.html', {"all_companies": all_companies})

'''Return the company view profile for the rest of the users in viewcompanyprofile.html'''
def company_view_profile(request, company_name):
    displayCompanyInViewCompanyPage = Company.objects.get(company_name=company_name) #used in viewcompanyprofile.html
    return render(request, 'e_declaratie_html_files/viewcompanyprofile.html', {"displayCompanyInViewCompanyPage": displayCompanyInViewCompanyPage})

'''Return all the users without the current user and admin in userlistpage.html'''
def users_list(request):
    all_users = User.objects.exclude(username=request.user).exclude(username='admin') #used in userlistpage.html
    return render(request, 'e_declaratie_html_files/userslistpage.html', {"all_users": all_users})

'''Return the user view profile in viewprofilepage.html for all the users'''
def user_view_profile(request, username):
    view_user = User.objects.get(username=username) #used in viewprofilepage.html
    return render(request, 'e_declaratie_html_files/viewprofilepage.html', {"view_user": view_user})

'''Update the user info, like username, first name, last name, etc'''
def update_user_info(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = EditUserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save() 
            messages.success(request, "Your profile was edited with success!")
            return redirect ('user_profile', user.username)
    else:
        form = EditUserInfoForm(instance=user)
    return render(request, 'e_declaratie_html_files/updateuserprofileinfo.html', { "form": form})
        
'''Update the company info, like name, email, etc'''
def update_company_info(request, company_name):
    the_company = Company.objects.get(company_name=company_name) #used in updatecompanyprofileinfo.html
    if request.method == "POST":
        form = EditCompanyInfoForm(request.POST, instance=the_company)
        if form.is_valid():
            form.save()
            messages.success(request, "Your company was edited with success!")
            return redirect ('company_profile', the_company.company_name)
    else:
        form = EditCompanyInfoForm(instance=the_company)
    return render(request, 'e_declaratie_html_files/updatecompanyprofileinfo.html', {"form": form, "the_company": the_company})

'''This function checked if the AddNewManagerForm is POST, take the input value and add to the managers field from Company table and return to the company page'''
def add_manager(request, company_name):
    get_company_name = Company.objects.get(company_name=company_name) #used in addmanagerpage.html
    if request.method == 'POST':
        form = AddNewManagerForm(request.POST)
        if form.is_valid():
            manager = form.cleaned_data['manager']
            get_company_name.managers.add(manager) #add the new manager at the company
            return redirect('company_profile', get_company_name.company_name)
    else:
        form = AddNewManagerForm()
    return render(request, 'e_declaratie_html_files/addmanagerpage.html', {'form': form, "get_company_name": get_company_name})

'''Delete the company account with conditions'''
def delete_company_account(request, company_name):
    company = Company.objects.get(company_name=company_name)
    company_managers = company.managers.all()

    if len(company_managers) == 1: #if you are the only one manager, then can delete the company
        company.delete()
        messages.success(request, "The company was successfully deleted!")
        return redirect('user_profile', request.user.username)
    elif len(company_managers) > 1: #if the company has more than one manager, you can't delete the company. You must delete all the managers first!.
        messages.warning(request, "If you want to delete the company, you must delete all the managers first!")
        return redirect('company_profile', company.company_name)

    return redirect('user_profile', request.user.username)

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