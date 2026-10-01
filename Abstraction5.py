from abc import ABC, abstractmethod


class Patient(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def __init__(self, name, days, room_rate_per_day):
        super().__init__(name)
        self.days = days
        self.room_rate = room_rate_per_day

    def calculate_bill(self):
        return self.days * self.room_rate + 5000       # + medicines/nursing

    def treatment(self):
        return "Admitted to ward with continuous monitoring."


class OutPatient(Patient):
    def __init__(self, name, consultation_fee):
        super().__init__(name)
        self.fee = consultation_fee

    def calculate_bill(self):
        return self.fee

    def treatment(self):
        return "Consultation and prescription; no admission required."


class EmergencyPatient(Patient):
    def __init__(self, name, severity_level):
        super().__init__(name)
        self.severity = severity_level

    def calculate_bill(self):
        return 10000 + self.severity * 5000

    def treatment(self):
        return "Immediate emergency care in ICU / trauma unit."


patients = [InPatient("Ravi", 4, 3000), OutPatient("Sunita", 500), EmergencyPatient("Arjun", 3)]
for p in patients:
    print(f"{p.name} ({type(p).__name__})")
    print("  Treatment:", p.treatment())
    print("  Bill     : Rs.", p.calculate_bill())
