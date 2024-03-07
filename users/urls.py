from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/edit-user/', views.update_user_info, name="update_user_info"),
    path('profile/<str:username>/change-password/', views.change_pass, name='change_pass'),
    path('delete-user/<int:user_id>/', views.delete_user_account, name="delete-user-account"),
    path('users-lists/', views.users_lists, name='users_lists'),
    path('users-list/profile/<str:username>/', views.user_view_profile, name='user_view_profile'),
    
]