from abc import ABC, abstractmethod


class Appointment(ABC):
    def __init__(self, patient_name):
        self.patient_name = patient_name

    @abstractmethod
    def book_appointment(self, slot):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self, slot):
        print(f"General appointment booked for {self.patient_name} at {slot}.")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def __init__(self, patient_name, specialty):
        super().__init__(patient_name)
        self.specialty = specialty

    def book_appointment(self, slot):
        print(f"{self.specialty} specialist appointment booked for {self.patient_name} at {slot}.")

    def calculate_fee(self):
        return 1500


class EmergencyAppointment(Appointment):
    def book_appointment(self, slot="Immediately"):
        print(f"EMERGENCY appointment booked for {self.patient_name}: {slot}.")

    def calculate_fee(self):
        return 3000


GeneralAppointment("Ravi").book_appointment("10:00 AM")
print("Fee: Rs.", GeneralAppointment("Ravi").calculate_fee())

sp = SpecialistAppointment("Sunita", "Cardiology")
sp.book_appointment("2:30 PM")
print("Fee: Rs.", sp.calculate_fee())

em = EmergencyAppointment("Arjun")
em.book_appointment()
print("Fee: Rs.", em.calculate_fee())
