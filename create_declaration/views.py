from django.shortcuts import render
from companies.models import Company
from companies.models import ExtendCompanyModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

'''This function is used to add a company stamp'''
@login_required(login_url='/login_user/')
def add_stamp(request, company_name):
    comp = Company.objects.get(company_name=company_name)
    company = ExtendCompanyModel.objects.get(extend_company_info=comp)
    
    if request.method == 'POST':
        try:
            company_stamp = request.FILES['company_stamp']
            company.company_stamp = company_stamp
            company.save()
            messages.success(request, "Stampila a fost adaugata cu succes!")
        except:
            messages.warning(request, "Ar trebui să alegeți mai întâi un fișier!")
              
    context = {
        "company": company,
        "comp": comp,
        }
    return render(request, 'declarations_html/addstamp.html', context)

'''This function is used to create a declaration'''
@login_required(login_url='/login_user/')
def create_declaration(request, company_name):
    company = Company.objects.get(company_name=company_name)
    
    context = {
        "company": company,
        }
    return render(request, 'create_default_pdf_html/createdeclaration.html', context)





