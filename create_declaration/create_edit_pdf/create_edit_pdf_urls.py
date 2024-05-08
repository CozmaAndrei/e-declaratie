from django.urls import path
from . import create_edit_pdf_views


urlpatterns = [
    path('edit-declaration/<str:company_name>/', create_edit_pdf_views.edit_declaration, name='edit_declaration'),
    path('preview-edit-pdf/<str:company_name>/', create_edit_pdf_views.preview_edit_pdf, name='preview_edit_pdf'),
    path('op2/<str:company_name>/', create_edit_pdf_views.client_input_op2, name='client_input_op2'),
    path('pdf_op2/<str:company_name>/', create_edit_pdf_views.pdf_to_client_op2, name='pdf_to_client_op2'),
]