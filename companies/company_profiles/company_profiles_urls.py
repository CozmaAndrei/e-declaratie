from django.urls import path
from . import company_profiles_views

urlpatterns = [
    path('company-profile/<str:company_name>/', company_profiles_views.company_view_profile, name='company_view_profile'),
    path('company-profile/<str:company_name>/report/', company_profiles_views.report_company, name='report_company'),     
]
