
# 📄 Document Extraction MVP 

## Overview
This project is a **Document Extraction MVP** built as part of the internship screening assignment for **Hyderabad Water Supply Board**.  
The system processes **long, complex PDFs (including scanned documents)** and extracts **structured information** that can be searched through a simple web interface.

The MVP focuses on **utility-style documents** and demonstrates an **end-to-end pipeline**:

**PDF ingestion → OCR & text extraction → structured field extraction → database storage → search UI**

The emphasis is on **functionality and clarity**, not a perfect or production-grade system.

---

## Chosen Assignment & Variant

- **Assignment**: Assignment 1 – Document Extraction MVP  
- **Variant**: **Variant D**
  - Document layout–aware extraction (page-wise processing)
  - OCR support using **Tesseract**
  - **PostgreSQL** database
  - **Flask-based** search interface
- **Domain**: **Water / Utility-style documents**

---

## Problem Statement
Government and utility departments handle large volumes of **PDF-based reports and billing documents**.  
These documents are often:

- Scanned or semi-structured  
- Hard to search  
- Manually reviewed for key fields  

This MVP demonstrates how such PDFs can be **automatically converted into structured, searchable data**, reducing manual effort and improving accessibility.

---

## What This MVP Extracts
From utility-style PDFs, the system extracts:

- **Member ID**
- **Payer Name**
- **Copay**
- **Page Number**

These fields are stored in a database and can be queried through an API.

---

## System Architecture

```

PDF
↓
PDF → Images (layout-aware)
↓
OCR (Tesseract)
↓
Text Processing & Entity Extraction
↓
PostgreSQL Database
↓
Flask Search API

```

---

## Folder Structure

```

pdf_ocr_mvp/
│
├── data/
│   └── input_pdfs/          # Input PDF documents
│
├── src/
│   ├── ingest_pdf.py        # PDF reading, layout handling, OCR
│   ├── extract_entities.py  # Extract member_id, payer_name, copay
│   ├── db.py                # PostgreSQL connection & table creation
│   ├── load_db.py           # Insert extracted records into DB
│   └── app.py               # Flask-based search API
├── requirements.txt         # Python dependencies
├── README.md

````

---

## How the Pipeline Works

### 1️⃣ PDF Ingestion
- The PDF is read **page-by-page**
- Each page is converted into an image to support **scanned documents**

### 2️⃣ OCR Processing
- **Tesseract OCR** extracts raw text from each page image

### 3️⃣ Entity Extraction
- The extracted text is parsed to identify:
  - Member ID
  - Payer Name
  - Copay
- Extraction is intentionally **rule-based** to keep the MVP simple and explainable

### 4️⃣ Database Storage
- Extracted fields are stored in **PostgreSQL**
- Each record is linked to its corresponding **page number**

### 5️⃣ Search Interface
- A **Flask API** allows:
  - Viewing all extracted records
  - Searching records by entity fields

---

## Setup & Run Instructions (Local)

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
````

Ensure the following system tools are installed:

* **Poppler**
* **Tesseract OCR**

On macOS:

```bash
brew install poppler tesseract
```

---

### 2️⃣ Start PostgreSQL

Ensure PostgreSQL is running locally.

Create the database:

```bash
createdb documents
```

---

### 3️⃣ Create Database Table

```bash
python3 -c "from src.db import create_table; create_table()"
```

---

### 4️⃣ Run PDF Extraction & Load Data

Place your PDF inside:

```
data/input_pdfs/
```

Run:

```bash
python3 src/load_db.py
```

---

### 5️⃣ Start the Flask App

```bash
python3 src/app.py
```

Access endpoints:

* **View all records**

  ```
  http://localhost:5001/all
  ```

* **Search by entity**

  ```
  http://localhost:5001/search?entity_id=H63098113
  ```

## Limitations

* Rule-based extraction (no full SLM integration yet)
* Limited to a small set of fields
* No advanced layout detection (tables, headers, footers)
* Minimal UI (API-based search)

---

## Future Improvements

* Integrate a **Small Language Model (SLM)** for flexible schema extraction
* Support multiple document types in parallel
* Add full-text search and filters
* Improve layout detection for tables and sections
* Add authentication and role-based access for government use

---

## Demo Video

The demo video shows:

* PDF ingestion
* OCR extraction
* Database insertion
* API-based search working end-to-end

---

## Conclusion

This MVP demonstrates a **practical, low-infrastructure approach** to document extraction suitable for **government and utility departments**.
It prioritizes **working functionality, clarity, and extensibility**, aligning with the assignment’s evaluation criteria.


