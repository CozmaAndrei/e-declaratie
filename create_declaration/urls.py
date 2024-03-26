from django.urls import path
from . import views

urlpatterns = [
    path('create-declaration/<int:company_id>/', views.create_declaration, name='create_declaration'),
    path('preview-default-pdf/<int:company_id>/<str:username>/', views.preview_default_pdf, name='preview_default_pdf'),
    path('add-stamp/<int:company_id>/', views.add_stamp, name='add_stamp'),
    path('edit-declaration/<int:company_id>/', views.edit_declaration, name='edit_declaration'),
    path('preview-edit-pdf/<int:company_id>/<str:username>', views.preview_edit_pdf, name='preview_edit_pdf'),
    path('op1/<str:username>/manager/<int:company_id>/', views.client_input_op1, name='client_input_op1'),
    path('op2/<str:username>/manager/<int:company_id>/', views.client_input_op2, name='client_input_op2'),
    path('pdf_op1/<str:company_id>/<str:username>/', views.pdf_to_client_op1, name='pdf_to_client_op1'),
    path('pdf_op2/<str:company_id>/<str:username>/', views.pdf_to_client_op2, name='pdf_to_client_op2')
]