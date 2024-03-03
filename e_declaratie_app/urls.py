from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('company-name/<str:company_name>/', views.company_profile, name='company_profile'), 
    path('companies-list/', views.companies_list, name='companies_list'),
    path('companies-list/<str:company_name>/', views.company_view_profile, name='company_view_profile'),
    
    
    
    path('companies-list/<str:company_name>/edit-company', views.update_company_info, name="update_company_info"),
    path('companies-list/<str:company_name>/add_manager/', views.add_manager, name='add_manager'),
    path('delete-company-account/<str:company_name>/', views.delete_company_account, name="delete-company-account"),
]