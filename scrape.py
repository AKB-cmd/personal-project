import fitz
import PyPDF2

pdf_path = 'C:/Users/Asus/OneDrive/Desktop/New folder/hydfcst.pdf'

# Using PyMuPDF (fitz)
print("Reading PDF with PyMuPDF (fitz):\n")
pdf_document = fitz.open(pdf_path)
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text = page.get_text()
    print(f'Page {page_num + 1}:\n{text}\n')