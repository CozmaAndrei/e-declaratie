from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import CustomAuthenticationForm
from .forms import CompanyRegisterForm
from users.models import ExtraUserInformations

# email activation imports start
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
# email activation imports


def login_user(request):
    '''Login function'''
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect ('user_profile', username=username)
    
    else: 
        form = CustomAuthenticationForm()
    return render(request, 'auth_html_files/login_user.html', {'form': form}) 
    
def logout_user(request):
    '''Logout function'''
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('login_user') 

def activateEmail(request, user, email):
    '''This function sends an email to the user with an activation link.'''
    mail_subject = 'Activate your account'
    message = render_to_string('auth_html_files/activate_account_email.html', {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(mail_subject, message, to=[email])
    if email.send():
        messages.success(request, f'Dear {user.first_name} {user.last_name} , please go to you email {user.email} inbox and click on received activation link to confirm and complete the registration. Note: Check your spam folder.')
    else:
        messages.error(request, 'An error occurred while sending the email. Please try again.')
    
def register_user(request):
    '''This function registers a user and sends an email to the user with an activation link.'''
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            user = form.save(commit=False)
            user.is_active = False # user cannot log in until the email is verified
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            date_of_birth = form.cleaned_data['date_of_birth']
            ExtraUserInformations.objects.create(user=user,date_of_birth=date_of_birth)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'auth_html_files/register_user.html', {'form': form})

def activate(request, uidb64, token):
    '''This function activates the user account.'''
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully!')
        return redirect('login_user')
    else:
        messages.warning(request, 'Activation link is invalid!')
        return redirect("home")  

def register_company(request):
    '''Company registration function'''
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            company = form.save()
            company.managers.add(request.user)
            company.save()
            extra_info, created = ExtraUserInformations.objects.get_or_create(user=request.user)
            extra_info.user_company.add(company)
            logout(request)
            messages.success(request, "Your company account was created, please Login!")
            return redirect('login_user')
    else:
        form = CompanyRegisterForm()
    return render(request, 'auth_html_files/register_company.html', {'form': form})
    