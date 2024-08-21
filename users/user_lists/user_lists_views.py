from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import ExtraUserInformations
from django.contrib.auth.decorators import login_required

'''Return all the users in the userslistspage.html and the favorite users in the userlistspage.html for the current user'''
@login_required(login_url='/login_user/')
def user_lists(request):
    all_users = User.objects.exclude(username=request.user).exclude(username='admin').order_by("username") #used in userlistpage.html and order by username (a-z)(All users)
    users = User.objects.get(username=request.user)
    extra_info = ExtraUserInformations.objects.get(user=users) #used in userlistpage.html (Favorite users)
    all_favorite_users = extra_info.favorite_user.all().order_by("username") #used in userlistpage.html (Favorite users)
    
    context = {
        "all_users": all_users,
        "all_favorite_users": all_favorite_users,
        "extra_info": extra_info
    }
    return render(request, 'user_lists_html/userslistspage.html', context)