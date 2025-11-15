class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} Edad: {self.edad}"

class Facultad:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.bailarines = []
    
    def agregar_bailarin(self, bailarin):
        if bailarin not in self.bailarines:
            self.bailarines.append(bailarin)
    
    def mostrar_bailarines(self):
        print(f"Bailarines de {self.nombre}:")
        for b in self.bailarines:
            print(f"  {b}")
    
    def __str__(self):
        return f"Facultad de {self.nombre}"

class Fraternidad:
    def __init__(self, nombre, color, encargado_nombre, encargado_apellido, 
                 encargado_edad, encargado_ci):
        self.nombre = nombre
        self.color = color
        self.encargado = Persona(encargado_nombre, encargado_apellido, 
                                encargado_edad, encargado_ci)
        self.bailarines = []
    
    def agregar_bailarin(self, bailarin):
        if bailarin not in self.bailarines:
            self.bailarines.append(bailarin)
    
    def mostrar_info(self):
        print(f"Fraternidad: {self.nombre} Color: {self.color}")
        print(f"Encargado: {self.encargado}")
        print(f"Bailarines: {len(self.bailarines)}")
        for b in self.bailarines:
            print(f" {b}")
    
    def __str__(self):
        return f"Fraternidad {self.nombre}"

class Bailarin:
    def __init__(self, nombre, apellido, edad, ci, facultad, fraternidad):
        self.datos_personales = Persona(nombre, apellido, edad, ci)
        self.facultad = facultad
        self.fraternidad = fraternidad
        
        self.facultad.agregar_bailarin(self)
        self.fraternidad.agregar_bailarin(self)
    
    def __str__(self):
        return (f"{self.datos_personales} "
                f"{self.facultad.nombre} Frat: {self.fraternidad.nombre}")

class SistemaGestion:
    def __init__(self):
        self.bailarines = []
        self.fraternidades = []
        self.facultades = []
    
    def registrar_bailarin(self, nombre, apellido, edad, ci, facultad, fraternidad):
        for b in self.bailarines:
            if b.datos_personales.ci == ci:
                if b.fraternidad != fraternidad:
                    print(f"No se puede registrar {nombre} {apellido} ya esta en {b.fraternidad.nombre}")
        
        nuevo_bailarin = Bailarin(nombre, apellido, edad, ci, facultad, fraternidad)
        self.bailarines.append(nuevo_bailarin)
        print(f"Bailarin registrado: {nuevo_bailarin}")
        return nuevo_bailarin
    
    def ver_todos_bailarines(self):
        print("LISTA DE BAILARINES:")
        for b in self.bailarines:
            print(f" {b}")
    
    def ver_edades_participantes(self):
        print("EDADES DE PARTICIPANTES:")
        for b in self.bailarines:
            print(f"{b.datos_personales.nombre} {b.datos_personales.apellido}: "
                  f"{b.datos_personales.edad} años")
    
    def verificar_fraternidades_duplicadas(self):
        print("VERIFICACION DE FRATERNIDADES DUPLICADAS:")
        problemas = False
        
        for i in range(len(self.bailarines)):
            for j in range(i + 1, len(self.bailarines)):
                if self.bailarines[i].datos_personales.ci == self.bailarines[j].datos_personales.ci:
                    if self.bailarines[i].fraternidad != self.bailarines[j].fraternidad:
                        print(f"{self.bailarines[i].datos_personales.nombre} esta en muchas fraternidades")
                        problemas = True
        
        if not problemas:
            print("Todos los bailarines estan en una sola fraternidad")

sistema = SistemaGestion()

fac_puras = Facultad("Ciencias Puras", "CP001")
fac_medicina = Facultad("Medicina", "MED001")
sistema.facultades.append(fac_puras)
sistema.facultades.append(fac_medicina)

frat_leones = Fraternidad("Los Leones", "Dorado", "Carlos", "Mendoza", 28, "12345678")
frat_tigres = Fraternidad("Los Tigres", "Naranja", "Maria", "Gonzalez", 26, "87654321")
sistema.fraternidades.append(frat_leones)
sistema.fraternidades.append(frat_tigres)

print("Registrando bailarines:")
b1 = sistema.registrar_bailarin("Juan", "Perez", 20, "111", fac_puras, frat_leones)
b2 = sistema.registrar_bailarin("Ana", "Lopez", 19, "222", fac_medicina, frat_leones)
b3 = sistema.registrar_bailarin("Pedro", "Ramos", 21, "333", fac_puras, frat_tigres)
b4 = sistema.registrar_bailarin("Sofia", "Torres", 20, "444", fac_medicina, frat_tigres)
b5 = sistema.registrar_bailarin("Luis", "Vargas", 22, "555", fac_puras, frat_leones)

print("\nIntentando registro duplicado:")
sistema.registrar_bailarin("Juan", "Perez", 20, "111", fac_puras, frat_tigres)

sistema.ver_todos_bailarines()
fac_puras.mostrar_bailarines()
fac_medicina.mostrar_bailarines()
frat_leones.mostrar_info()
frat_tigres.mostrar_info()
sistema.ver_edades_participantes()
sistema.verificar_fraternidades_duplicadas()