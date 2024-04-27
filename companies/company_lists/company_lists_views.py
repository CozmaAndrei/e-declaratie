from django.shortcuts import render, redirect
from django.contrib import messages
from companies.models import Company
from users.models import ExtraUserInformations


'''Return all the companies without the current user company in companieslistpage.html'''
def company_lists(request):
    all_companies = Company.objects.exclude(managers=request.user) #used in for loop in companieslistpage.html
    companies = ExtraUserInformations.objects.get(user=request.user) #used in companieslistpage.html
    favorite_companies = companies.favorite_company.all() #used in companieslistpage.html
    
    context = {
        "all_companies": all_companies,
        "companies": companies,
        "favorite_companies": favorite_companies
        }
    return render(request, 'company_lists_html/companieslistpage.html', context)