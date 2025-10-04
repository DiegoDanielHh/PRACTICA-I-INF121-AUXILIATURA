from multimethod import multimethod

class Empleado:
    def __init__(self, nombre, sueldoMes):
        self.nombre = nombre
        self.sueldoMes = sueldoMes

    @multimethod
    def sueldoTotal(self):
        return self.sueldoMes


class Administrativo(Empleado):
    def __init__(self, nombre, sueldoMes, cargo):
        super().__init__(nombre, sueldoMes)
        self.cargo = cargo


class Chef(Empleado):
    def __init__(self, nombre, sueldoMes, horaExtra, tipo, sueldoHora):
        super().__init__(nombre, sueldoMes)
        self.horaExtra = horaExtra
        self.tipo = tipo
        self.sueldoHora = sueldoHora

    @multimethod
    def sueldoTotal(self):
        return self.sueldoMes + (self.horaExtra * self.sueldoHora)


class Mesero(Empleado):
    def __init__(self, nombre, sueldoMes, propina, horaExtra, sueldoHora):
        super().__init__(nombre, sueldoMes)
        self.propina = propina
        self.horaExtra = horaExtra
        self.sueldoHora = sueldoHora

    @multimethod
    def sueldoTotal(self):
        return self.sueldoMes + (self.horaExtra * self.sueldoHora) + self.propina

empleados = [
    Chef("Remy", 3000, horaExtra=10, tipo="Pastelero", sueldoHora=50),
    Mesero("Linguini", 2000, propina=300, horaExtra=5, sueldoHora=20),
    Mesero("Colette", 2100, propina=250, horaExtra=8, sueldoHora=25),
    Administrativo("Skinner", 2500, cargo="Gerente"),
    Administrativo("Django", 2200, cargo="Contador")
]


X = 2200
print(f"Empleados con sueldoMes = {X}:")
for e in empleados:
    if e.sueldoMes == X:
        print(f"- {e.nombre} ({type(e).__name__})")

print("\nSueldos totales de los empleados:")
for e in empleados:
    print(f"{e.nombre} ({type(e).__name__}): {e.sueldoTotal()}")
