from pdf2image import convert_from_path
import pytesseract

def ingest_pdf(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)
    results = []

    for idx, page in enumerate(pages, start=1):
        text = pytesseract.image_to_string(page)
        results.append({
            "page_number": idx,
            "text": text
        })

    return results
