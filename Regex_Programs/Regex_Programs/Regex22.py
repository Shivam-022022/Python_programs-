import re

invoice = """
Invoice No: INV-2026-0042
Date: 12-10-2026
Customer: Sharma Traders
Item A ......... Rs. 1,250.50
Item B ......... Rs. 3,000
GST (18%) ...... Rs. 765.09
Total Amount: INR 5,015.59
Due Date: 26/10/2026
"""

invoice_numbers = re.findall(r"Invoice\s*(?:No\.?|Number|#)\s*[:\-]?\s*([A-Z0-9-]+)", invoice, re.I)
dates = re.findall(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b", invoice)
amounts = re.findall(r"(?:Rs\.?|INR)\s*\d[\d,]*(?:\.\d{1,2})?", invoice)

print("Invoice numbers:", invoice_numbers)
print("Dates          :", dates)
print("Amounts        :", amounts)
