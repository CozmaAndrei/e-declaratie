from django.shortcuts import render
from user_company_app.models import Company

#pdf import start
from django.http import FileResponse, HttpResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from django.conf import settings
from django.templatetags.static import static
#pdf import stop

def create_declaration(request, company_id):
    '''what this function do ?'''
    company = Company.objects.get(id=company_id)
    
    context = {
        "company": company
        }
    return render(request, 'declarations_html/createdeclaration.html', context)

# def preview_default_pdf(request):
    
#     #Create Bytestream buffer
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
#     width, height = letter
#     #Create a text object
#     textobject = p.beginText()
#     textobject.setTextOrigin(inch, inch)
#     textobject.setFont("Helvetica", 12)
    
#     #Add text to the text object
#     lines = [
#         "Hello, this is a test pdf file.",
#     ]
    
#     #loop
#     for line in lines:
#         textobject.textLine(line)
    
#     #Save the text object to the canvas 
#     p.drawText(textobject)
#     p.showPage()
#     p.save()
#     buffer.seek(0)
    
#     #return the pdf file
#     return FileResponse(buffer, filename='testPDF.pdf')

def preview_default_pdf(request, company_id):
    company = Company.objects.get(id=company_id)
    buffer = io.BytesIO()  # Create a BytesIO buffer
    w, h = A4  # Get the width and height of the A4 page
    c = canvas.Canvas(buffer, pagesize=A4)  # Create a canvas with A4 page size
    textobject = c.beginText(400, 760)  # Create a text object
    textobject.textLine(f'{company.company_name}')
    textobject.textLine(f'')
    textobject.textLine(f'CUI:{company.company_cui}')# Add text to the text object
    textobject.textLine(f'{company.company_register_number}')
    textobject.textLine(f'Localitate:{company.company_city}')
    textobject.textLine(f'Adresa:{company.company_address}')
    textobject.textLine(f'Telefon:{company.contact_person_phone}')
    # Add the logo image to the canvas
    if not company.company_logo:
        textobject.textLine('')  # Add text to the text object
    else:
        logo_path = company.company_logo.path  # Use .path instead of .url
        c.drawImage(logo_path, 50, 650, width=150, height=150)  # Add an image to the canvas
    
    # Add the text object to the canvas
    c.drawText(textobject)  # Draw the text object on the canvas
    c.showPage()
    c.save()
    buffer.seek(0)  # Move the buffer cursor to the beginning
    return FileResponse(buffer, filename='testPDF.pdf')  # Pass the buffer to FileResponse
