# Create a project directory containing packages for:
#   a) Patient management
#   b) Doctor management
#   c) Billing
#   d) Medical records
# Implement simple functions in each module and access them from main.py.
#
# NOTE: A real project would use "patient/", "doctor/", "billing/", and
# "medical_records/" packages. It is simulated here in one file using
# clearly labelled sections so it matches the file-XX.py naming
# convention used for this exercise set.

# ---------- patient package ----------
patients = {}


def register_patient(patient_id, name, age):
    patients[patient_id] = {"name": name, "age": age}
# ---------- end patient package ----------


# ---------- doctor package ----------
doctors = {}


def register_doctor(doctor_id, name, specialization):
    doctors[doctor_id] = {"name": name, "specialization": specialization}
# ---------- end doctor package ----------


# ---------- billing package ----------
def generate_bill(patient_id, consultation_fee, medicine_charges):
    total = consultation_fee + medicine_charges
    return {"patient_id": patient_id, "total": total}
# ---------- end billing package ----------


# ---------- medical_records package ----------
medical_records = {}


def add_medical_record(patient_id, diagnosis, prescription):
    medical_records[patient_id] = {"diagnosis": diagnosis, "prescription": prescription}
# ---------- end medical_records package ----------


if __name__ == "__main__":
    register_patient("P01", "Ritesh Agale", 21)
    register_doctor("D01", "Dr. Mehta", "General Physician")
    add_medical_record("P01", "Common Cold", "Paracetamol")
    bill = generate_bill("P01", 300, 150)

    print(f"Patient: {patients['P01']}")
    print(f"Doctor: {doctors['D01']}")
    print(f"Medical Record: {medical_records['P01']}")
    print(f"Bill: {bill}")
