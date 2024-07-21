import PyPDF2

pdf_path = 'C:/Users/Asus/OneDrive/Desktop/New folder/hydfcst.pdf'

# Using PyPDF2
print("Reading PDF with PyPDF2:\n")
with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        print(f'Page {page_num + 1}:\n{text}\n')
