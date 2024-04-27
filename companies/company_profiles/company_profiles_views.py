from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from companies.models import Company
from users.models import ExtraUserInformations
from .company_profiles_forms import ReportCompanyForm
from django.conf import settings
from django.contrib import messages

'''Return the company view profile for the rest of the users in viewcompanyprofile.html'''
def company_view_profile(request, company_name):
    company = Company.objects.get(company_name=company_name) #used in viewcompanyprofile.html
    current_user_profile = ExtraUserInformations.objects.get(user=request.user)  # Get the ExtraUserInformations instance for the current user
    if request.method == "POST":
        action = request.POST.get("follow")
        if action == "unfollow":
            current_user_profile.favorite_company.remove(company)
        elif action == "follow":
            current_user_profile.favorite_company.add(company)
        current_user_profile.save()
    
    context = {
        "company": company,
        "current_user_profile": current_user_profile
    }
    return render(request, 'company_profiles_html/viewcompanyprofile.html', context)

'''This function will help users to report the other company'''
def report_company(request, company_name):
    company_report = Company.objects.get(company_name=company_name)
    if request.method == "POST":
        report_form = ReportCompanyForm(request.POST)
        if report_form.is_valid():
            reason = report_form.cleaned_data['reason']
            description = report_form.cleaned_data['description']
            #send email to admin
            mail_subject= f"Firma {company_report.company_name} a fost raportata de {request.user.username}"
            body= f"Firma: {company_report.company_name} a fost raportata de {request.user.username} pentru urmatorul:\nMotiv: {reason}.\nDescriere: {description}."
            email = EmailMessage(mail_subject, body, reply_to=[request.user.email,company_report.company_email], to=[settings.EMAIL_HOST_USER])
            if email.send():
                messages.error(request, f'Multumim pentru raport. Vom investiga problema și vom lua măsurile corespunzătoare.')
                return redirect('company_view_profile', company_name=company_report.company_name)
    else:
        report_form = ReportCompanyForm()
        
    context = {
        "company_report": company_report,
        "report_form": report_form,
    }
    return render(request, 'company_profiles_html/reportcompany.html', context)

