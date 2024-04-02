from django.shortcuts import render
from user_company_app.models import Company
from user_company_app.models import ExtendCompanyModel
from django.contrib import messages


def add_stamp(request, company_id):
    '''This function is used to add a company stamp'''
    company = ExtendCompanyModel.objects.get(extend_company_info=company_id)
    if request.method == 'POST':
        try:
            company_stamp = request.FILES['company_stamp']
            company.company_stamp = company_stamp
            company.save()
            messages.success(request, "The company stamp was added with success!")
        except:
            messages.warning(request, "You should choose a file first!")
              
    context = {
        "company": company,
        }
    return render(request, 'declarations_html/addstamp.html', context)

def create_declaration(request, company_id):
    company = Company.objects.get(id=company_id)
    
    context = {
        "company": company,
        
        }
    return render(request, 'create_default_pdf_html/createdeclaration.html', context)





