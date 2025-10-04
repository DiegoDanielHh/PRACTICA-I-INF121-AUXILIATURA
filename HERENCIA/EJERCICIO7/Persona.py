# Clase base Persona
class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self._nombre = nombre      
        self._paterno = paterno    
        self._materno = materno    
        self._edad = edad          

class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, regProfesional):
        super().__init__(nombre, paterno, materno, edad)
        self.__sueldo = sueldo                    
        self.__regProfesional = regProfesional    
    
    def mostrar(self):
        print(f"Docente: {self._nombre} {self._paterno} {self._materno}")
        print(f"Edad: {self._edad}")
        print(f"Sueldo: {self.__sueldo}")
        print(f"Registro Profesional: {self.__regProfesional}")

class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.__ru = ru              
        self.__matricula = matricula    
    
    def mostrar(self):
        print(f"Estudiante: {self._nombre} {self._paterno} {self._materno}")
        print(f"Edad: {self._edad}")
        print(f"RU: {self.__ru}")
        print(f"Matrícula: {self.__matricula}")
    
    def modificarEdad(self, nueva_edad):
        self._edad = nueva_edad
        print(f"Edad modificada a: {nueva_edad}")

estudiante1 = Estudiante("Juan", "Pérez", "González", 20, "202001234", "MAT2024-001")
estudiante2 = Estudiante("María", "López", "Martínez", 22, "202001235", "MAT2024-002")
docente1 = Docente("Carlos", "Ramírez", "Flores", 45, 8500, "REG-12345")

estudiante1.mostrar()
print()
estudiante2.mostrar()
print()
docente1.mostrar()

def promedio(estudiantes):
    suma_edades = sum(est._edad for est in estudiantes)
    promedio_edad = suma_edades / len(estudiantes)
    return promedio_edad

lista_estudiantes = [estudiante1, estudiante2]
print(f"Promedio de edad de los estudiantes: {promedio(lista_estudiantes)}")

print(f"Edad actual de {estudiante1._nombre}: {estudiante1._edad}")
estudiante1.modificarEdad(21)

if estudiante1._edad == docente1._edad:
    print(f"{estudiante1._nombre} tiene la misma edad que el docente")
else:
    print(f"{estudiante1._nombre} NO tiene la misma edad que el docente")

if estudiante2._edad == docente1._edad:
    print(f"{estudiante2._nombre} tiene la misma edad que el docente")
else:
    print(f"{estudiante2._nombre} NO tiene la misma edad que el docente")