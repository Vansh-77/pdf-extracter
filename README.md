# PDF Data Extraction Web App

A web-based backend application that allows users to upload PDF files, extract structured data from them, and store the results in MongoDB.  
Built as a proof-of-work for PDF processing, API design, and database integration.

---

##  Features

- Web interface for uploading PDF files  
- Backend API built with Flask  
- Text extraction from PDFs using `pdfplumber`  
- Structured data parsing (invoice-style PDFs)  
- MongoDB integration for persistent storage  
- JSON API responses  
- Easily extensible for OCR or additional fields  

---

##  Tech Stack

- **Backend**: Python, Flask  
- **PDF Parsing**: pdfplumber  
- **Database**: MongoDB (PyMongo)  
- **Frontend**: HTML, CSS, JavaScript  
- **Environment**: Local development  

---

## 📁 Project Structure

```text
pdf-data-extractor/
│
├── app.py                # Flask application
├── pdf_parser.py         # PDF extraction logic
├── db.py                 # MongoDB connection
│
├── templates/
│   └── index.html        # Web upload page
│
├── samples/
│   └── sample_invoice.pdf
│
├── requirements.txt
└── README.md 
```
--- 

## 🔧 Setup & Installation

### 1️⃣ Clone the repository

git clone https://github.com/Vansh-77/pdf-extracter.git 
cd pdf-data-extractor  

### 2️⃣ Install dependencies

pip install -r requirements.txt  

### 3️⃣ Start MongoDB

mongod  

(Or use MongoDB Compass / MongoDB Atlas)

---

## ▶️ Running the Application

python app.py  

The app will run at:

http://127.0.0.1:5000

---

## 📤 Uploading a PDF

1. Open the web interface  
2. Select a PDF file  
3. Click Upload  

The extracted data is:  
- Returned as JSON  
- Stored in MongoDB  

---

## 📡 API Endpoint

### POST /upload-pdf

Request  
- multipart/form-data  
- Field name: file  

Response  

{
  "status": "success",
  "document_id": "65f9c2e9e3f1a8...",
  "data": {
    "invoice_number": "INV-1024",
    "customer_name": "John Doe",
    "total_amount": 500.0
  }
}
