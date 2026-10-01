class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} (Age {self.age})")


class Doctor(Person):                       # hierarchical: Person -> Doctor
    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization

    def display(self):
        super().display()
        print("  Specialization:", self.specialization)


class Patient(Person):                      # hierarchical: Person -> Patient
    def __init__(self, ailment, **kwargs):
        super().__init__(**kwargs)
        self.ailment = ailment

    def display(self):
        super().display()
        print("  Ailment:", self.ailment)


class Researcher(Person):                   # helper class for multiple inheritance
    def __init__(self, research_area, **kwargs):
        super().__init__(**kwargs)
        self.research_area = research_area

    def display(self):
        super().display()
        print("  Research Area:", self.research_area)


class Surgeon(Doctor):                      # multilevel: Person -> Doctor -> Surgeon
    def __init__(self, surgeries_done, **kwargs):
        super().__init__(**kwargs)
        self.surgeries_done = surgeries_done

    def display(self):
        super().display()
        print("  Surgeries Performed:", self.surgeries_done)


class MedicalResearcher(Doctor, Researcher):    # multiple inheritance
    def __init__(self, publications, **kwargs):
        super().__init__(**kwargs)
        self.publications = publications

    def display(self):
        super().display()
        print("  Publications:", self.publications)


print("--- Doctor ---")
Doctor(name="Dr. Mehta", age=45, specialization="Cardiology").display()
print("--- Patient ---")
Patient(name="Ravi", age=52, ailment="Hypertension").display()
print("--- Surgeon ---")
Surgeon(name="Dr. Iyer", age=50, specialization="Neurosurgery", surgeries_done=1200).display()
print("--- Medical Researcher ---")
mr = MedicalResearcher(name="Dr. Kapoor", age=42, specialization="Oncology",
                       research_area="Cancer Immunotherapy", publications=35)
mr.display()
print("MRO:", [c.__name__ for c in MedicalResearcher.__mro__])
