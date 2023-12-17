import PyPDF2
import sys


# ---------------------------------------------
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        print(f'{pdf} successfully merged')
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)

# ---------------------------------------------

# # 'rb' as read binary
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
