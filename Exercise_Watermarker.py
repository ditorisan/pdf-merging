# Import the PyPDF2 library
import PyPDF2

# Open the PDF files - 'super.pdf' as the template and 'wtr.pdf' as the watermark
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))

# Create a PdfWriter object for the output PDF
output = PyPDF2.PdfWriter()

# Iterate through each page of the template PDF
for i in range(len(template.pages)):
    # Get the current page from the template
    page = template.pages[i]

    # Merge the current page with the first page of the watermark PDF
    page.merge_page(watermark.pages[0])

    # Add the merged page to the output PDF
    output.add_page(page)

# Write the output PDF to a new file named 'watermarked.pdf'
with open('watermarked.pdf', 'wb') as file:
    output.write(file)
