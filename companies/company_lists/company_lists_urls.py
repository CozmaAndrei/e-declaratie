from django.urls import path, include
from . import company_lists_views

urlpatterns = [
    path('company-lists/', company_lists_views.company_lists, name='company_lists'),
]