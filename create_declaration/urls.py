from django.urls import path
from . import views

urlpatterns = [
    path('create-declaration/<str:company_name>/', views.create_declaration, name='create_declaration')
    
]