from abc import ABC, abstractmethod
class IPersona(ABC):
    @abstractmethod
    def mostrar_datos_personales(self):
        pass
    
class IEmpleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class IPolicia(ABC):
    @abstractmethod
    def mostrar_rango(self):
        pass

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado:
    def __init__(self, sueldo, codigo):
        self.sueldo = sueldo
        self.codigo = codigo

class Policia:
    def __init__(self, grado, unidad):
        self.grado = grado
        self.unidad = unidad

class JefePolicia(Persona, Empleado, Policia, IPersona, IEmpleado, IPolicia):
    def __init__(self, nombre, edad, sueldo, codigo, grado, unidad):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, sueldo, codigo)
        Policia.__init__(self, grado, unidad)
    
    def mostrar_datos_personales(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def calcular_salario(self):
        return self.sueldo
    
    def mostrar_rango(self):
        return f"Grado: {self.grado}, Unidad: {self.unidad}"
    
    def mostrar_datos(self):
        print(f"Jefe de Policía: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Código: {self.codigo}")
        print(f"Sueldo: {self.sueldo}")
        print(f"Grado: {self.grado}")
        print(f"Unidad: {self.unidad}")

jefe1 = JefePolicia("Roberto Gómez", 45, 12000, "POL-001", "Coronel", "Unidad Táctica")
jefe2 = JefePolicia("Ana Martínez", 42, 15000, "POL-002", "Coronel", "Unidad de Investigación")

print("JEFE 1:")
jefe1.mostrar_datos()
print("\nJEFE 2:")
jefe2.mostrar_datos()

if jefe1.sueldo > jefe2.sueldo:
    print(f"El jefe con mayor sueldo es: {jefe1.nombre} con un sueldo de {jefe1.sueldo}")
elif jefe2.sueldo > jefe1.sueldo:
    print(f"El jefe con mayor sueldo es: {jefe2.nombre} con un sueldo de {jefe2.sueldo}")
else:
    print(f"Ambos tienen el mismo sueldo: {jefe1.sueldo}")

if jefe1.grado == jefe2.grado:
    print(f"Ambos jefes tienen el mismo grado: {jefe1.grado}")
else:
    print(f"Los jefes tienen diferentes grados: {jefe1.nombre} es {jefe1.grado} y {jefe2.nombre} es {jefe2.grado}")

print(f"\nDatos personales de {jefe1.nombre}: {jefe1.mostrar_datos_personales()}")
print(f"Salario calculado: {jefe1.calcular_salario()}")
print(f"Rango: {jefe1.mostrar_rango()}")