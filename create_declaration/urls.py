from django.urls import path, include
from . import views

urlpatterns = [
    path('create-declaration/<str:company_name>/', views.create_declaration, name='create_declaration'),
    path('add-stamp/<str:company_name>/', views.add_stamp, name='add_stamp'),
    path('', include('create_declaration.create_default_pdf.create_default_pdf_urls')),
    path('', include('create_declaration.create_edit_pdf.create_edit_pdf_urls')), 
]