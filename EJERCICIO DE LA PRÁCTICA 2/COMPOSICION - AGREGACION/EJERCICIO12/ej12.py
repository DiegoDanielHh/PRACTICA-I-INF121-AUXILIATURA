class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Doctor: {self.nombre} Especialidad: {self.especialidad}"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def mostrar_doctores(self):
        print(f"Doctores en el hospital: {self.nombre}")
        if not self.doctores:
            print("No hay doctores asignados.")
        else:
            for d in self.doctores:
                print(f"{d}")

d1 = Doctor("Juan Perez", "Cardiología")
d2 = Doctor("Luis Perez", "Pediatría")
d3 = Doctor("Maria Gomez", "Neurología")

h1 = Hospital("Hospital Central")
h2 = Hospital("Hospital no tan central")

h1.agregar_doctor(d1)
h1.agregar_doctor(d2)

h2.agregar_doctor(d2)
h2.agregar_doctor(d3)

h1.mostrar_doctores()
h2.mostrar_doctores()
