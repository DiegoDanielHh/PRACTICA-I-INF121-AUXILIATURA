class Politico:
    def __init__(self, profesion, añosExp):
        self.profesion = profesion
        self.añosExp = añosExp

class Partido:
    def __init__(self, nombreP, rol):
        self.nombreP = nombreP
        self.rol = rol

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, añosExp, nombreP, rol):
        Politico.__init__(self, profesion, añosExp)
        Partido.__init__(self, nombreP, rol)
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar(self):
        print(f"Presidente: {self.nombre} {self.apellido}")
        print(f"Profesión: {self.profesion}")
        print(f"Años de Experiencia: {self.añosExp}")
        print(f"Partido: {self.nombreP}")
        print(f"Rol: {self.rol}")

presidente1 = Presidente("Luis", "Arce", "No sabe nada al parecer", 30, "MAS", "Destructor de la pais")

nombre = "Evaristo"
apellido = "Morales"
profesion = "Ni idea"
años = 25
partido = "MAS"
rol = "Sigue siendo destructor del pais"
presidente2 = Presidente(nombre, apellido, profesion, años, partido, rol)

presidente1.mostrar()
print()
presidente2.mostrar()

presidentes = [
    Presidente("Luis", "Arce", "Economista", 30, "MAS", "Destructor de la pais"),
    Presidente("Evaristo", "Morales", "Ni idea", 25, "MAS", "Sigue siendo destructor del pais"),
    Presidente("Carlos", "Mesa", "Periodista", 35, "Comunidad Ciudadana", "Candidato")
]

nombre_buscar = "Evaristo"

encontrado = False
for presidente in presidentes:
    if presidente.nombre == nombre_buscar:
        print(f"\nPresidente encontrado: {presidente.nombre} {presidente.apellido}")
        print(f"Partido Político: {presidente.nombreP}")
        print(f"Profesión: {presidente.profesion}")
        encontrado = True
        break

if not encontrado:
    print(f"\nNo se encontró ningún presidente con el nombre: {nombre_buscar}")