from django.shortcuts import render
from user_company_app.models import Company

# Create your views here.

def create_declaration(request, company_name):
    company = Company.objects.get(company_name=company_name)
    
    context = {
        "company": company
        }
    return render(request, 'declarations_html/createdeclaration.html', context)