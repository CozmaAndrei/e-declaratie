from django.shortcuts import render
from companies.models import Company
from companies.models import ExtendCompanyModel
from django.contrib import messages


'''This function is used to add a company stamp'''
def add_stamp(request, company_id):
    company = ExtendCompanyModel.objects.get(extend_company_info=company_id)
    comp = Company.objects.get(id=company_id)
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
def create_declaration(request, company_id):
    company = Company.objects.get(id=company_id)
    
    context = {
        "company": company,
        }
    return render(request, 'create_default_pdf_html/createdeclaration.html', context)





