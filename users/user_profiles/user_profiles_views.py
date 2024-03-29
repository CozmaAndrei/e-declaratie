from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import ExtraUserInformations


def user_view_profile(request, username):
    '''Return the user view profile in viewprofilepage.html for all the users and the current user profile in viewprofilepage.html for the current user'''
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