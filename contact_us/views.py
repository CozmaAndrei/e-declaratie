from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

'''This function sends an email to the admin with the contact form data.'''
def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            
            mail_subject = f"Trimitere formular de contact de la {name}"
            message = f"Nume: {name}\nEmail: {email}\nMesaj: {message}"
            
            email = EmailMessage(mail_subject, message, reply_to=[email], to=[settings.EMAIL_HOST_USER])
            if email.send():   
                messages.success(request, f'Vă mulțumim că ne-ați contactat, {name}! Vom reveni cât mai curând posibil.')
                return redirect('contact_us')
    else:
        contact_form = ContactForm()
    
    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact_us_html/contactpage.html', context)
