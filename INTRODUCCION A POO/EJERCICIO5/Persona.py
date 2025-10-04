class Persona:
    def __init__(self,nombre, paterno, materno, edad,ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci
    
    def mostrarDatos(self):
        return f"El nombre es: {self.nombre}, el paterno es: {self.paterno}, el materno es: {self.materno}, la edad es: {self.edad} y el CI es: {self.ci}"
    
    def mayorDeEdad(self):
        if self.edad >= 18:
            return f"La persona es mayor de edad"
        else:
            return f"la persona es menor de edad"
        
    def modificarEdad(self,nuevo):
        self.edad = nuevo
        return f"ACTUALIZACION: La nueva edad es {self.edad}"

print("PERSONA 1")
o1=Persona("Juan", "Perez", "Pozo", 20, 12345678)
print(o1.mostrarDatos())
print(o1.mayorDeEdad())
print(o1.modificarEdad(17)) 
print() 
print("PERSONA 2")
o2=Persona("Pedro", "Perez", "Arroyo", 17, 98765432)
print(o2.mostrarDatos())
print(o2.mayorDeEdad())
print(o2.modificarEdad(30))    
print() 
print("VERIFICANDO EL APELLIDO")
if o1.paterno == o2.paterno:
    print("Tienen el mismo apellido paterno")
else:
    print("No tienen el mismo apellido paterno")     