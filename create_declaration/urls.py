from django.urls import path
from . import views

urlpatterns = [
    path('create-declaration/<int:company_id>/', views.create_declaration, name='create_declaration'),
    path('preview-default-pdf/<int:company_id>/', views.preview_default_pdf, name='preview_default_pdf'),
    path('add-stamp/<int:company_id>/', views.add_stamp, name='add_stamp'),
]