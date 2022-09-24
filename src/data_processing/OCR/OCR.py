import pytesseract
from pdf2image import convert_from_path
import glob

TESSERACT_EXE = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSERACT_DATA = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
TESSERACT_POPPLER = r'C:\Users\User\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'


def get_ocr_file(path: str) -> str:
    pdfs = glob.glob(rf"{path}")
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_EXE
    tessdata_dir_config = TESSERACT_DATA
    poppler_path = TESSERACT_POPPLER

    all_text = []
    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
        for pageNum, imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob, lang='rus', config=tessdata_dir_config)
            all_text.append(text)
    return ' '.join(all_text)

