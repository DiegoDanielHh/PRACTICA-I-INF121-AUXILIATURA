class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__sueldo = sueldo
    
    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSueldo(self):
        return self.__sueldo
    
    def setSueldo(self, nuevosueldo):
        self.__sueldo = nuevosueldo
        
        
class Departamento:
    def __init__(self,nombre, area):
        self.__nombre = nombre
        self.__area = area
        self.__empleados = []
        
    def mostrarEmpleados(self):
        print(f"Departamento: {self.__nombre} - Area: {self.__area}")
        if not self.__empleados:
            print("No existen empleados")
        else:
            for i in self.__empleados:
                print(f"nombre: {i.getNombre()}, cargo: {i.getCargo()} y sueldo: {i.getSueldo()}")
        
    def cambioSalario(self, nuevosalario):
        for i in self.__empleados:
            i.setSueldo(nuevosalario)
            
    def getEmpleados(self):
        return self.__empleados
    
    def setEmpleados(self,vectorEmpleados):
        self.__empleados = vectorEmpleados
        
     
        
        
dep1 = Departamento("Recursos humanos","Administracion")
dep2 = Departamento("Investigación","Desarrollo")
e1 = Empleado("Ana","Analista",3000)
e2 = Empleado("Luis","Asistente", 2500)
e3 = Empleado("Marta", "Jefa", 5000)
e4 = Empleado("Pablo", "Reclutador", 2800)
e5 = Empleado("Sonia", "Psicóloga", 3200)
vectorEmpleadosd1 = [e1,e2,e3,e4,e5]
dep1.setEmpleados(vectorEmpleadosd1)
dep1.mostrarEmpleados()
dep2.mostrarEmpleados()
print("Aplicando el cambio de salario")
dep1.cambioSalario(4000)
dep1.mostrarEmpleados()
print("VERIFICACION DE EMPLEADOS: ")
cont = 0
for i in dep1.getEmpleados():
    if i in dep2.getEmpleados():
        cont +=1
if cont>0:
    print("Existe un empleado de dep1 en dep2")
else:
    print("No existe un empleado de dep1 en dep2")
print("MOVIENDO EMPLEADOS")
for i in dep1.getEmpleados():
    dep2.getEmpleados().append(i)
dep1.setEmpleados([])
dep1.mostrarEmpleados()
dep2.mostrarEmpleados()
        
        