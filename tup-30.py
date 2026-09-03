# Problem Statement:
# Lowest score
# Average score
# Create two tuples and find the common elements between them.
# Merge two tuples and remove duplicate elements.
# Count the frequency of each element in a tuple.
# Convert a tuple into a sorted tuple in ascending and descending order.
# Create a tuple containing patient records:
# Patient ID
# Name
# Age
# Blood Group
# Perform the following operations:
# Display all records
# Search for a patient by ID
# Count the total number of patients
# Display patients with a specific blood group

# Answer:
patients = (
    (101, "Ritesh", 21, "A+"),
    (102, "Amit", 22, "B+"),
    (103, "Sneha", 20, "O+")
)

print("All records:")
for patient in patients:
    print(patient)

patient_id = int(input("Enter patient ID: "))
found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:", patient)
        found = True
        break

if not found:
    print("Patient not found")

print("Total patients:", len(patients))

blood_group = input("Enter blood group: ")
print("Patients with", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
