from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import ExtraUserInformations
from django.core.mail import EmailMessage
from .user_profiles_forms import ReportUserForm
from django.contrib import messages

'''Return the user view profile in viewprofilepage.html for all the users and the current user profile in viewprofilepage.html for the current user'''
def user_view_profile(request, username):
    view_user = User.objects.get(username=username) #used in viewprofilepage.html
    extra_view_user_info = ExtraUserInformations.objects.get(user=view_user) #request in ExtraUserInformations model for table fields
    current_user_profile = request.user.extrauserinformations
    if request.method == "POST":
        action = request.POST.get("follow")
        if action == "unfollow":
            current_user_profile.favorite_user.remove(view_user)
        elif action == "follow":
            current_user_profile.favorite_user.add(view_user)
        current_user_profile.save()
    
    context = {
        "view_user": view_user,
        "extra_view_user_info": extra_view_user_info,
        "current_user_profile": current_user_profile
    }
    return render(request, 'user_profiles_html/viewprofilepage.html', context)

'''Report a user, send an email to the admin and return the reportuser.html page'''
def report_user(request, username):
    report_user = User.objects.get(username=username)
    if request.method == "POST":
        report_form = ReportUserForm(request.POST)
        if report_form.is_valid():
            reason = report_form.cleaned_data['reason']
            description = report_form.cleaned_data['description']
            #send email to admin
            mail_subject= f"Userul {report_user.username} este raportat de {request.user.username}"
            body= f"Userul: {report_user.username} ({report_user.first_name} {report_user.last_name}) este raportat de {request.user.username} ({request.user.first_name} {request.user.last_name}) pentru următoarele:\nMotivul: {reason}.\nDescriere: {description}."
            email = EmailMessage(mail_subject, body, reply_to=[request.user.email], to=[settings.EMAIL_HOST_USER])
            if email.send():
                messages.error(request, f'Multumim pentru raport. Vom investiga problema și vom lua măsurile corespunzătoare.')
                return redirect('user_view_profile', username=username)
    else:
        report_form = ReportUserForm()
        
    context = {
        "report_user": report_user,
        "report_form": report_form
    }
    return render (request, 'user_profiles_html/reportuser.html', context)