from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_profile, name='user_profile'),
    path('<str:username>/edit-user/', views.update_user_info, name="update_user_info"),
    path('<str:username>/change-password/', views.change_pass, name='change_pass'),
    path('delete-user/<int:user_id>/', views.delete_user_account, name="delete-user-account"),
    path('users-list/', views.users_list, name='users_list'),
    path('users-list/<str:username>/', views.user_view_profile, name='user_view_profile'),
    
]