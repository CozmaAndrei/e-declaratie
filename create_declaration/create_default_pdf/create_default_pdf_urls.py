from django.urls import path
from . import create_default_pdf_views

urlpatterns = [
    path('preview-default-pdf/<int:company_id>/<str:username>/', create_default_pdf_views.preview_default_pdf, name='preview_default_pdf'),
    path('op1/<str:company_name>/', create_default_pdf_views.client_input_op1, name='client_input_op1'),
    path('pdf_op1/<str:company_id>/<str:username>/', create_default_pdf_views.pdf_to_client_op1, name='pdf_to_client_op1'),
    
]






