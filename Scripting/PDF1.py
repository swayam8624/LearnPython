import pypdf
import sys

with open('dummy.pdf', mode='rb') as file:
    reader = pypdf.PdfReader(file)
    print(reader)
    writer = pypdf.PdfWriter()
    writer.add_page(reader.pages[0])
    # rotation
    writer.pages[0].rotate(90)  #clockwise
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
    # pdf merger
    # terminal command = python pdf1.py file1.pdf fil2.pdf ...

    inputs = sys.argv[1:]


    def pdf_combiner(pdf_list):
        for pdf in pdf_list:
            writer.append(pdf)
            print(pdf)
        writer.write('super.pdf')
        writer.close()
pdf_combiner(inputs)
file.close()

# Watermarker

template = pypdf.PdfReader(open('super.pdf','rb'))
watermark = pypdf.PdfReader(open('wtr.pdf','rb'))
output = pypdf.PdfWriter()
for i in range(template.get_num_pages()):
    page = template.get_page(i)
    page.merge_page(watermark.get_page(0)) # not using standard merger, as it merges page with watermark
    output.add_page(page)
    with open("watermark.pdf" , 'wb') as new_file:
        output.write(new_file)

