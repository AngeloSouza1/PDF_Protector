from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
import os

def modify_pdf(filename, cpf, position, color, upload_folder):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    # Define the coordinates for each corner
    if position == 'top-left':
        x = 50
        y = 800
    elif position == 'top-right':
        x = 500
        y = 800
    elif position == 'bottom-left':
        x = 50
        y = 50
    elif position == 'bottom-right':
        x = 500
        y = 50
    else:
        raise ValueError('Invalid position')

    # Draw main text (in orange)
    can.setFillColor(color)  # Set fill color
    can.setFont("Helvetica", 8)  # Set font to Helvetica, size 8
    can.drawString(x, y, cpf)
    can.save()

    try:
        packet.seek(0)
        new_pdf = PdfReader(packet)
        print("Successfully created new PDF with CPF.")
    except Exception as e:
        print("Error creating new PDF with CPF: " + str(e))
        return  # Exit function in case of an error

    try:
        existing_pdf_path = os.path.join(upload_folder, filename)
        existing_pdf = PdfReader(open(existing_pdf_path, "rb"))
        print("Successfully opened existing PDF.")
        output = PdfWriter()
        print(f"Number of pages in existing PDF: {len(existing_pdf.pages)}")

        for i in range(len(existing_pdf.pages)):
            page = existing_pdf.pages[i]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)

        with open(existing_pdf_path, "wb") as outputStream:
            output.write(outputStream)

        print(f"Modified PDF saved at: {existing_pdf_path}")

    except Exception as e:
        print("Error opening or modifying existing PDF: " + str(e))
