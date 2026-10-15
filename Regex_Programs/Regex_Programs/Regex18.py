import re

paragraph = ("Send the parcel to 12 MG Road, Pune 411001 or to Andheri, Mumbai 400053. "
             "Ignore the order number 0123456 and phone 9876543210.")

pins = re.findall(r"\b[1-9]\d{5}\b", paragraph)
print("PIN codes found:", pins)
