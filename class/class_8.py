class Patient:

    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)

    def calculate_total_bill(self, extra_charges):
        return self.consultation_fee + extra_charges


patient_id = input("Enter patient ID: ")
name = input("Enter name: ")
age = int(input("Enter age: "))
disease = input("Enter disease: ")
consultation_fee = float(input("Enter consultation fee: "))

patient = Patient(patient_id, name, age, disease, consultation_fee)
patient.display_info()

extra_charges = float(input("Enter extra charges (medicine/tests): "))
print("Total Bill =", patient.calculate_total_bill(extra_charges))