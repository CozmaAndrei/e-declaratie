from linecache import getlines
from django.shortcuts import render
from user_company_app.models import Company

#pdf imports start
from django.http import FileResponse, HttpResponse
import io
import os
from django.conf import settings
import textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  A4
from reportlab.lib.utils import ImageReader
from django.templatetags.static import static
from django.contrib.staticfiles import finders
#pdf imports stop

def create_declaration(request, company_id):
    '''what this function do ?'''
    company = Company.objects.get(id=company_id)
    context = {
        "company": company,
        
        }
    return render(request, 'declarations_html/createdeclaration.html', context)

def default_content(request, default_text, company_id):
    company = Company.objects.get(id=company_id)
    default_text = f'{ company.company_name } avand sediu social in {company.company_city}, str. {company.company_address}, inregistrata cu nr. {company.company_register_number} la Registrul Comertului, CUI {company.company_cui}, reprezentata de {request.user.first_name} {request.user.last_name}, in calitate de Administrator, declaram pe propria raspundere, cunoscand prevederile art.292 Cod Penal cu privire la falsul in declaratii si preverile art. 5 din HG nr.1022/2002 cu privire la regimul produselor si serviciilor care pot pune in pericol viata, sanatatea,securitatea muncii si protectia mediului, faptul ca produsele din factura nr ((((((?)))))) din data de ((((((?)))))) care fac obiectul acestei declaratii de conformitate nu pune in pericol viata, sanatatea si securitatea muncii, nu produce impact negativ asupra mediului si este in conformitate cu normele Uniunii Europene.'
    return default_text

def preview_default_pdf(request, company_id):
    
    company = Company.objects.get(id=company_id)
    
    # Create a BytesIO buffer
    buffer = io.BytesIO()
    
    # Get the width and height of the A4 page
    w, h = A4 
    
    # Create a canvas with A4 page size
    c = canvas.Canvas(buffer, pagesize=A4)  
    
    # add the title of the pdf
    c.setTitle(f'Declaratie de conformitate pentru {company.company_name}')

    # Add the company logo or default logo to the pdf in the left top corner
    if not company.company_logo:
        # Add the default logo image to the canvas
        default_logo_path = finders.find('images/defaultCompanyLogo.png')
        c.drawImage(default_logo_path, 50, 650, width=150, height=150)  
    else:
        # Add the company logo image to the canvas
        logo_path = company.company_logo.path
        c.drawImage(logo_path, 50, 650, width=150, height=150, preserveAspectRatio=True)
        
    # Add the company informations in right top corner
    c.drawRightString(520, 775, f'{company.company_name.upper()}')
    c.drawRightString(520, 760, f'')
    c.drawRightString(520, 745, f'CUI:{company.company_cui.upper()}')
    c.drawRightString(520, 730, f'{company.company_register_number.upper()}')
    c.drawRightString(520, 715, f'Localitate:{company.company_city.upper()}')
    c.drawRightString(520, 700, f'Adresa:{company.company_address.upper()}')
    c.drawRightString(520, 685, f'Email:{company.company_email.upper()}')
    if company.contact_person_phone:
        c.drawRightString(520, 670, f'Telefon:{company.contact_person_phone.upper()}')

    # The title of the declaration
    title_of_declaration = c.beginText(170, 580)
    title_of_declaration.setFont("Helvetica", 16)
    title_of_declaration.textLine(f'DECLARATIE DE CONFORMITATE')
    
    # The second title of the declaration
    second_title_of_declaration = c.beginText(235, 550)
    second_title_of_declaration.setFont("Helvetica", 12)
    second_title_of_declaration.textLine(f'1 din data 05.10.2023')
    
    # The content of the declaration
    text_x = 60
    text_y = 480
    text_lines = ""  # Define the variable "text_lines"
    max_text_width = 90  # Maximum width of the text

    # Write the text
    content = default_content(request, text_lines, company_id)
    # Wrap text to fit within max width
    wrapped_lines = textwrap.wrap(content, width=max_text_width)
    
    # Draw text lines
    for line in wrapped_lines:
        c.drawString(text_x, text_y, line)
        text_y -= 20  # space between lines
    else:
        c.drawString(60, text_y - 20, "Aceasta declaratie de conformitate, are valabilitate 180 de zile de la data emiteri.")
        text_y -= 20
        c.drawString(60, text_y - 60, f'{company.company_name}')
        text_y -= 60
        c.drawString(60, text_y - 20, f'prin reprezentatul legal {request.user.first_name} {request.user.last_name}')
     
    # Add the text object to the canvas
    c.drawText(title_of_declaration)
    c.drawText(second_title_of_declaration)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, filename=f'Declaratie de conformitate {company.company_name}.pdf')
