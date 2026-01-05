import pdfplumber
import io
import re

def extract_data(pdf_bytes):
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages)

    return {
        "invoice_number": re.search(r"Invoice\s*No:\s*(\S+)", text).group(1),
        "customer_name": re.search(r"Customer:\s*(.+)", text).group(1),
        "total_amount": float(
            re.search(r"Total:\s*\$([\d.]+)", text).group(1)
        ),
        "raw_text": text
    }
