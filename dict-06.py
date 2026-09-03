# Create a dictionary of employee IDs and names. Ask the user for an
# employee ID and check whether it exists.

def check_employee_exists(employee_dict, emp_id):
    return emp_id in employee_dict


if __name__ == "__main__":
    employees = {"E01": "Amit", "E02": "Priya", "E03": "Rohan"}
    print(f"Employees: {employees}")

    emp_id = input("Enter employee ID to check: ")
    exists = check_employee_exists(employees, emp_id)
    print(f"{emp_id} {'exists' if exists else 'does not exist'}")
