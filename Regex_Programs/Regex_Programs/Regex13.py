import re

paragraph = ("The project started on 05-01-2026 and the first review was held on 15-03-2026. "
             "Final submission is due on 30-06-2026. Ignore 32-13-2026 and 2026-01-05.")

pattern = r"\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b"

dates = re.findall(pattern, paragraph)
print("Dates found (DD-MM-YYYY):", dates)
