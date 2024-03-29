from django.urls import include, path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/edit-user/', views.update_user_info, name="update_user_info"),
    path('profile/<str:username>/change-password/', views.change_pass, name='change_pass'),
    path('delete-user/<int:user_id>/', views.delete_user_account, name="delete-user-account"),
    path('users-list/', include('users.user_lists.user_lists_urls')), #include the user_lists_urls.py from user_lists folder
    path('users-list/', include('users.user_profiles.user_profiles_urls')), #include the user_profiles_urls.py from user_profiles folder
    
]