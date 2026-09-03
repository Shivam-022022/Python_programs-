# Problem Statement:
# Create a tuple of employee IDs and find the index of a given ID.

# Answer:
employee_ids = (101, 102, 103, 104, 105)
employee_id = int(input("Enter employee ID: "))
if employee_id in employee_ids:
    print(employee_ids.index(employee_id))
else:
    print("ID not found")
