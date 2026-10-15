import re

# Format: 2 letters (state) + 2 digits (RTO) + 1-2 letters (series) + 4 digits
pattern = r"[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}"

reg_no = input("Enter vehicle registration number (e.g. MH12AB1234): ").strip().upper()
reg_no = re.sub(r"[\s-]", "", reg_no)          # allow spaces/hyphens while typing

if re.fullmatch(pattern, reg_no):
    print(reg_no, "is a valid vehicle registration number format.")
else:
    print(reg_no, "is NOT a valid vehicle registration number format.")
