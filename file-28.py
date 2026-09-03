# Create a module containing functions to calculate gross salary,
# deductions, and net salary for an employee.
#
# NOTE: Combined into a single file. The "salary module" section below
# represents what would normally live in a separate salary_utils.py file.

# ---------- salary module ----------
def gross_salary(basic, hra_percent=20, da_percent=15):
    hra = basic * hra_percent / 100
    da = basic * da_percent / 100
    return basic + hra + da


def deductions(gross, pf_percent=12, tax_percent=10):
    pf = gross * pf_percent / 100
    tax = gross * tax_percent / 100
    return pf + tax


def net_salary(basic):
    gross = gross_salary(basic)
    total_deductions = deductions(gross)
    return gross - total_deductions
# ---------- end salary module ----------


if __name__ == "__main__":
    basic = 30000
    print(f"Gross Salary: {gross_salary(basic):.2f}")
    print(f"Deductions: {deductions(gross_salary(basic)):.2f}")
    print(f"Net Salary: {net_salary(basic):.2f}")
