from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from companies.models import Company
from users.models import ExtraUserInformations
from .company_profiles_forms import ReportCompanyForm
from django.conf import settings
from django.contrib import messages


def company_view_profile(request, company_name):
    '''Return the company view profile for the rest of the users in viewcompanyprofile.html'''
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

def report_company(request, company_name):
    company_report = Company.objects.get(company_name=company_name)
    if request.method == "POST":
        report_form = ReportCompanyForm(request.POST)
        if report_form.is_valid():
            reason = report_form.cleaned_data['reason']
            description = report_form.cleaned_data['description']
            #send email to admin
            mail_subject= f"Company {company_report.company_name} reported by {request.user.username}"
            body= f"Company: {company_report.company_name} has been reported by {request.user.username} for the following:\nReason: {reason}.\nDescription: {description}."
            email = EmailMessage(mail_subject, body, reply_to=[request.user.email,company_report.company_email], to=[settings.EMAIL_HOST_USER])
            if email.send():
                messages.error(request, f'Thank you for reporting. We will investigate the issue and take appropriate action.')
                return redirect('company_view_profile', company_name=company_report.company_name)
    else:
        report_form = ReportCompanyForm()
        
    context = {
        "company_report": company_report,
        "report_form": report_form,
    }
    return render(request, 'company_profiles_html/reportcompany.html', context)

