from ingest_pdf import ingest_pdf
from extract_entities import extract_entities
from db import get_connection

PDF_PATH = '/Users/sibanitiwari08/Desktop/pdf_ocr_mvp/data/input_pdfs/INS VERI 03 22 2024.65440.pdf'

pages = ingest_pdf(PDF_PATH)

conn = get_connection()
cur = conn.cursor()

for page in pages:
    record = extract_entities(page)

    # skip empty pages
    if not record["entity_id"]:
        continue

    cur.execute("""
    INSERT INTO documents (page_number, member_id, payer_name, copay)
    VALUES (%s, %s, %s, %s)
""", (
    record["page_number"],
    record["entity_id"],
    record["payer_name"],
    record["copay"]
))


conn.commit()
cur.close()
conn.close()

print("✅ PDF data extracted and loaded into DB")
