from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile-name/<str:username>/', views.user_profile, name='user_profile'),
    path('company-name/<str:company_name>/', views.company_profile, name='company_profile'), 
    path('companies-list/', views.companies_list, name='companies_list'),
    path('companies-list/<str:company_name>/', views.company_view_profile, name='company_view_profile'),
    path('users-list/', views.users_list, name='users_list'),
    path('users-list/<str:username>/', views.user_view_profile, name='user_view_profile'),
    path('profile-name/<str:username>/edit-user/', views.update_user_info, name="update_user_info"),
    path('companies-list/<str:company_name>/edit-company', views.update_company_info, name="update_company_info"),
    path('companies-list/<str:company_name>/add_manager/', views.add_manager, name='add_manager'),
    path('delete-company-account/<str:company_name>/', views.delete_company_account, name="delete-company-account"),
    path('delete-user/<int:user_id>/', views.delete_user_account, name="delete-user-account"),
    
    
]