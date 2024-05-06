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

'''Login function'''
def login_user(request):
    if request.method == "POST":
        login_form = CustomAuthenticationForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect ('user_profile', username=username)
    
    else: 
        login_form = CustomAuthenticationForm()
    
    context = {
        'login_form': login_form
    }
    return render(request, 'auth_html_files/login_user.html', context) 

'''Logout function'''  
def logout_user(request):
    logout(request)
    return redirect('home') 

'''This function sends an email to the user with an activation link.'''
def activateEmail(request, user, email): 
    mail_subject = 'Activeaza cont eDeclaratie'
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
        messages.success(request, f'{user.first_name} {user.last_name}, mergeti la email-ul {user.email} in inbox și faceți click pe linkul de activare primit pentru a confirma și finaliza înregistrarea. Note: Verificati si folderul spam.')
        return redirect ('home')
    else:
        messages.error(request, 'A apărut o eroare la trimiterea e-mailului. Vă rugăm să încercați din nou.')
        return redirect ('home')

'''This function registers a user and sends an email to the user with an activation link.'''  
def register_user(request):
    if request.method == 'POST': 
        register_user_form = UserRegisterForm(request.POST) 
        if register_user_form.is_valid(): 
            user = register_user_form.save(commit=False)
            user.is_active = False # user cannot log in until the email is verified
            user.save()
            activateEmail(request, user, register_user_form.cleaned_data.get('email'))
            ExtraUserInformations.objects.create(user=user)
            return redirect('home')
    else:
        register_user_form = UserRegisterForm()
        
    context = {
        'register_user_form': register_user_form
    }
    return render(request, 'auth_html_files/register_user.html', context)

'''This function activates the user account.'''
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Contul tau a fost activat cu succes!')
        return redirect('login_user')
    else:
        messages.warning(request, 'Link-ul de activare este invalid! Incercati sa va inregistrati din nou!')
        return redirect("home")  

'''Company registration function'''
def register_company(request):
    if request.method == 'POST':
        register_company_form = CompanyRegisterForm(request.POST)
        if register_company_form.is_valid():
            company = register_company_form.save()
            company.managers.add(request.user)
            company.company_manager = request.user
            company.save()
            extra_info, created = ExtraUserInformations.objects.get_or_create(user=request.user)
            extra_info.user_company.add(company)
            return redirect('company_profile', company_name=company.company_name)
    else:
        register_company_form = CompanyRegisterForm()
        
    context = {
        'register_company_form': register_company_form,
    }
    return render(request, 'auth_html_files/register_company.html', context)
    