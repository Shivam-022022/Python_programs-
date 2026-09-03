# Create a dictionary containing employee names and salaries. Find:
# - Highest salary
# - Lowest salary
# - Average salary
# - Employees earning more than Rs. 50,000

def highest_salary(salary_dict):
    return max(salary_dict, key=salary_dict.get)


def lowest_salary(salary_dict):
    return min(salary_dict, key=salary_dict.get)


def average_salary(salary_dict):
    return sum(salary_dict.values()) / len(salary_dict)


def employees_above_50k(salary_dict):
    return {name: sal for name, sal in salary_dict.items() if sal > 50000}


if __name__ == "__main__":
    salaries = {"Amit": 45000, "Priya": 62000, "Rohan": 38000, "Sneha": 71000}

    print(f"Salaries: {salaries}")
    print(f"Highest paid: {highest_salary(salaries)}")
    print(f"Lowest paid: {lowest_salary(salaries)}")
    print(f"Average salary: {average_salary(salaries):.2f}")
    print(f"Earning more than 50000: {employees_above_50k(salaries)}")
