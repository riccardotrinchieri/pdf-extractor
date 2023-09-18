import pytesseract
import PyPDF2
from pdf2image import convert_from_bytes

def extract_text_directly(file):
    pdf = PyPDF2.PdfReader(file)
    result = ""
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        result += page.extract_text()
    
    if result.strip():
        return result,  True
    return None, False


def extract_text_from_image(file, first_page=None, last_page=None):

    pages = convert_from_bytes(file, first_page=first_page, last_page=last_page)

    text = ''
    for page in pages:
        text += pytesseract.image_to_string(page) + '\n'
     
    return text