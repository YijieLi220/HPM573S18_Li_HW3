class Patient():
    def __init__(self, name):
        self.name = name
    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(Patient):
    def discharge(self):
        print("Name: ", self.name)
        print("Kind: ", "Emergency Patient")
        return "Emergency"

class HospitalizedPatient(Patient):
    def discharge(self):
        print("Name: ", self.name)
        print("Kind: ", "Hospitalized Patient")
        return "Hospitalize"

class Hospital():
    def __init__(self):
        self.cost = 0
        self.patients = []
    def admit(self, patient):
        self.patients.append(patient)
    def discharge_all(self):
        for p in self.patients:
            kind = p.discharge()
            if kind == "Emergency":
                self.cost += 1000
            elif kind == "Hospitalize":
                self.cost += 2000
    def get_total_cost(self):
            print("the total cost: ", str(self.cost))
            return self.cost

h = Hospital();
p1 = HospitalizedPatient("Jay")
h.admit(p1)
p2 = HospitalizedPatient("Sam")
h.admit(p2)
p3 = EmergencyPatient("Tom")
h.admit(p3)
p4 = EmergencyPatient("Lee")
h.admit(p4)
p5 = EmergencyPatient("Susan")
h.admit(p5)

h.discharge_all()
h.get_total_cost()