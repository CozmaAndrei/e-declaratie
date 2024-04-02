from django.shortcuts import render, redirect
from companies.models import Company
from companies.models import ExtendCompanyModel
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from create_declaration.forms import MyForm

#pdf imports start
from django.http import FileResponse
import io
import textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.contrib.staticfiles import finders
#pdf imports stop

def edit_declaration(request, company_id):
    '''Edit the declaration content for a company. If the declaration content is not set, it will be set to a default value. If the form is submitted, the new content will be saved in the database.'''
    company = Company.objects.get(id=company_id)
    user = User.objects.get(username=request.user)
    extended_company = ExtendCompanyModel.objects.get(extend_company_info=company_id)
    edited_text = f'{company.company_name.upper()} avand sediu social in localitatea {company.company_city.upper()}, adresa {company.company_address.upper()}, inregistrata cu nr. {company.company_register_number} la Registrul Comertului, CUI {company.company_cui}, reprezentata de {user.first_name.upper()} {user.last_name.upper()}, in calitate de Administrator, declaram pe propria raspundere, cunoscand prevederile art.292 Cod Penal cu privire la falsul in declaratii si preverile art. 5 din HG nr.1022/2002 cu privire la regimul produselor si serviciilor care pot pune in pericol viata, sanatatea, securitatea muncii si protectia mediului, faptul ca produsele din factura cu nr *invoice_number* din data de *invoice_date* care fac obiectul acestei declaratii de conformitate nu pune in pericol viata, sanatatea si securitatea muncii, nu produce impact negativ asupra mediului si este in conformitate cu normele Uniunii Europene.'
    
    if request.method == 'POST':
        if 'reset' in request.POST:
            form = MyForm(initial={"text": edited_text})
        else:
           form = MyForm(request.POST, initial={"text": edited_text}) 
        if form.is_valid():
            text = form.cleaned_data.get('text')
            extended_company.declaration_content = text
            extended_company.save()
    else:
        if extended_company.declaration_content:
            form = MyForm(initial={"text": extended_company.declaration_content})
        else:
            form = MyForm(initial={"text": edited_text})       

    context = {
        "form": form,
        'company': company,
        'extended_company': extended_company,
        }
    return render(request, 'create_edit_pdf_html/editdeclaration.html', context)

def edited_text(edit_text, company_id, username, invoice_number, invoice_date):
    '''This functions is used to return the text from the ExtendedCompanyModel and replace the placeholders with the invoice number and date.'''
    extended_company = ExtendCompanyModel.objects.get(extend_company_info=company_id)
    edit_text = extended_company.declaration_content
    if edit_text:
        edit_text = edit_text.replace("*invoice_number*", str(invoice_number))
        edit_text = edit_text.replace("*invoice_date*", str(invoice_date))
    return edit_text

def preview_edit_pdf(request, company_id, username):
    '''This function is used to create a preview pdf for the edited declaration.'''
    user = User.objects.get(username=username)
    company = Company.objects.get(id=company_id)
    stamp = ExtendCompanyModel.objects.get(extend_company_info=company_id)   

    # Get the text input and date input from the form
    if request.method == "POST":
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        if invoice_date and invoice_number:  # Check that invoice_date is not empty
            new_format = datetime.strptime(invoice_date, '%Y-%m-%d')
            new_formatted_invoice_date = new_format.strftime('%d-%m-%Y')
        else:
            messages.warning(request, "You should choose an invoice number and date first!")
            return redirect('edit_declaration', company_id=company_id)
    
    # Create a BytesIO buffer
    buffer = io.BytesIO()
    
    # Get the width and height of the A4 page
    w, h = A4 
    
    # Create a canvas with A4 page size
    c = canvas.Canvas(buffer, pagesize=A4)  
    
    # add the title of the pdf
    c.setTitle(f'Preview Declaratie de conformitate pentru {company.company_name}')
    
    # Add the company logo or default logo to the pdf in the left top corner
    if not company.company_logo:
        # Add the default logo image to the canvas
        default_logo_path = finders.find('images/defaultCompanyLogo.png')
        c.drawImage(default_logo_path, 70, 660, width=130, height=130)  
    else:
        # Add the company logo image to the canvas
        logo_path = company.company_logo.path
        c.drawImage(logo_path, 70, 660, width=130, height=130, preserveAspectRatio=True)
        
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
    title_of_declaration = c.beginText(170, 600)
    title_of_declaration.setFont("Helvetica", 16)
    title_of_declaration.textLine(f'DECLARATIE DE CONFORMITATE')
    
    # The second title of the declaration
    second_title_of_declaration = c.beginText(235, 580)
    second_title_of_declaration.setFont("Helvetica", 12)
    second_title_of_declaration.textLine(f'1 din data {new_formatted_invoice_date}')
    # The content of the declaration
    axa_x = 45
    axa_y = 540
    text_lines = ""  # Define the variable "text_lines"
    max_text_width = 85  # Maximum chars of the text

    # Write the text
    content = edited_text(text_lines, company_id, username, invoice_number, new_formatted_invoice_date)
    c.setFont("Helvetica", 12)
    
    # Wrap text to fit within max width
    if content is not None:
        wrapped_lines = textwrap.fill(content, width=max_text_width, break_long_words=True, break_on_hyphens=True).split('\n')
    else:
        wrapped_lines = []
    
    # Draw text lines
    for line in wrapped_lines:
        c.drawString(axa_x, axa_y, line)
        axa_y -= 20  # space between lines
    else:
        c.drawString(45, axa_y - 20, "Aceasta declaratie de conformitate, are valabilitate 180 de zile de la data emiteri.")
        axa_y -= 20
        c.drawString(45, axa_y - 60, f'{company.company_name.upper()}')
        axa_y -= 60
        c.drawString(45, axa_y - 20, f'prin reprezentatul legal {user.first_name.upper()} {user.last_name.upper()}')
        axa_y -= 160
        # Add the company stamp to the pdf
        if not stamp.company_stamp:
            # do nothing
            pass
        else:
            # Add the company stamp image to the canvas
            stamp_path = stamp.company_stamp.path
            c.drawImage(stamp_path, 80, axa_y, width=100, height=100, preserveAspectRatio=True)
        
    # Add the text object to the canvas
    c.drawText(title_of_declaration)
    c.drawText(second_title_of_declaration)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, filename=f'Preview Declaratie de conformitate {company.company_name}.pdf')

def client_input_op2(request, company_id, username):
    '''This function is used to send the pdf to the client.'''
    user = User.objects.get(username=username)
    company = Company.objects.get(id=company_id)
    
    context= {
        'company': company,
        'user': user,
    }
    return render (request, 'create_edit_pdf_html/clientURL2.html', context)

def pdf_to_client_op2(request, company_id, username):
    '''This function is used to create the pdf and send it to the client.'''
    user = User.objects.get(username=username)
    company = Company.objects.get(id=company_id)
    stamp = ExtendCompanyModel.objects.get(extend_company_info=company_id)   

    # Get the text input and date input from the form
    if request.method == "POST":
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        if invoice_date and invoice_number:  # Check that invoice_date is not empty
            new_format = datetime.strptime(invoice_date, '%Y-%m-%d')
            new_formatted_invoice_date = new_format.strftime('%d-%m-%Y')
        else:
            messages.warning(request, "You should choose an invoice number and date first!")
            return redirect('client_input_op2', company_id=company_id, username=username)
    
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
        c.drawImage(default_logo_path, 70, 660, width=130, height=130)  
    else:
        # Add the company logo image to the canvas
        logo_path = company.company_logo.path
        c.drawImage(logo_path, 70, 660, width=130, height=130, preserveAspectRatio=True)
    
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
    title_of_declaration = c.beginText(170, 600)
    title_of_declaration.setFont("Helvetica", 16)
    title_of_declaration.textLine(f'DECLARATIE DE CONFORMITATE')
    
    # The second title of the declaration
    second_title_of_declaration = c.beginText(235, 580)
    second_title_of_declaration.setFont("Helvetica", 12)
    second_title_of_declaration.textLine(f'1 din data {new_formatted_invoice_date}')
    
    # The content of the declaration
    axa_x = 45
    axa_y = 540
    text_lines = ""  # Define the variable "text_lines"
    max_text_width = 85  # Maximum chars of the text

    # Write the text
    content = edited_text(text_lines, company_id, username, invoice_number, new_formatted_invoice_date)
    c.setFont("Helvetica", 12)
    # Wrap text to fit within max width
   # Wrap text to fit within max width
    if content is not None:
        wrapped_lines = textwrap.fill(content, width=max_text_width, break_long_words=True, break_on_hyphens=True).split('\n')
    else:
        wrapped_lines = []
    
    # Draw text lines
    for line in wrapped_lines:
        c.drawString(axa_x, axa_y, line)
        axa_y -= 20  # space between lines
    else:
        c.drawString(45, axa_y - 20, "Aceasta declaratie de conformitate, are valabilitate 180 de zile de la data emiteri.")
        axa_y -= 20
        c.drawString(45, axa_y - 60, f'{company.company_name.upper()}')
        axa_y -= 60
        c.drawString(45, axa_y - 20, f'prin reprezentatul legal {user.first_name.upper()} {user.last_name.upper()}')
        axa_y -= 160
        # Add the company stamp to the pdf
        if not stamp.company_stamp:
            # do nothing
            pass
        else:
            # Add the company stamp image to the canvas
            stamp_path = stamp.company_stamp.path
            c.drawImage(stamp_path, 80, axa_y, width=100, height=100, preserveAspectRatio=True)
    
    # Add the text object to the canvas
    c.drawText(title_of_declaration)
    c.drawText(second_title_of_declaration)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, filename=f'Declaratie de conformitate {company.company_name}.pdf')
