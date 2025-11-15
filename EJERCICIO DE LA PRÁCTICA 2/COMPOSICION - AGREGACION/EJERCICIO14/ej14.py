class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return f"Nombre:{self.nombre} Puesto:{self.puesto} Salario:{self.salario}Bs"


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_info(self):
        print(f"Empresa: {self.nombre}")
        print("Empleados:")
        for e in self.empleados:
            print(e)

    def buscar_empleado(self, nombre):
        for e in self.empleados:
            if e.nombre == nombre:
                return e

    def eliminar_empleado(self, nombre):
        nuevos_empleados = []
        for e in self.empleados:
            if e.nombre != nombre:
                nuevos_empleados.append(e)
        self.empleados = nuevos_empleados

    def promedio_salarial(self):
        if not self.empleados:
            return 0
        total = 0
        for e in self.empleados:
            total += e.salario
        return total / len(self.empleados)

    def empleados_con_salario_mayor(self, valor):
        resultado = []
        for e in self.empleados:
            if e.salario > valor:
                resultado.append(e)
        return resultado

empresa = Empresa("La Gran Empresa")
empresa.agregar_empleado(Empleado("Juan", "Ingeniera", 3000))
empresa.agregar_empleado(Empleado("Luis", "Secretario", 2500))
empresa.agregar_empleado(Empleado("Pedro", "Gerente", 4000))
empresa.mostrar_info()

print("\nBuscando a Luis: ")
empleado = empresa.buscar_empleado("Luis")
if empleado:
    print(empleado)
else:
    print("Empleado no encontrado")

empresa.eliminar_empleado("Juan")
print("\nDespus de eliminar a Juan:")
empresa.mostrar_info()
print("\nPromedio salarial:", empresa.promedio_salarial())
print("Empleados con salario mayor a 3000: ")
for e in empresa.empleados_con_salario_mayor(3000):
    print(e)
