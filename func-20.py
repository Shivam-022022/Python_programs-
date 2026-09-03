# Write a function that accepts basic salary and calculates gross salary after
# adding HRA and DA.

def gross_salary(basic):
    hra = 0.20 * basic
    da = 0.15 * basic
    return basic + hra + da


if __name__ == "__main__":
    basic = float(input("Enter basic salary: "))
    print(f"Gross Salary = Rs. {gross_salary(basic):.2f}")
