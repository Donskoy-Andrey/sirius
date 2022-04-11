import pytesseract
from pdf2image import convert_from_path
import glob


def get_ocr_file(path):
    pdfs = glob.glob(rf"{path}")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # path to tesseract.exe
    tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'  # path to tessdata
    poppler_path = r'C:\Users\User\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'  # path to poppler
    all_text = []
    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
        for pageNum, imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob, lang='rus', config=tessdata_dir_config)
            all_text.append(text)
    return ' '.join(all_text)