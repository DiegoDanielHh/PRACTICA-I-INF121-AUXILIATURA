class Crucero:
    def __init__(self):
        self.__nombre = ""
        self.__paisOrigen = ""
        self.__paisDestino = ""
        self.__nroPasajeros = 0
        self.__pasajeros = [] 
    
    def __pos__(self):
        print("--- Ingreso de datos del Crucero ---")
        self.__nombre = input("Nombre del crucero: ")
        self.__paisOrigen = input("País de origen: ")
        self.__paisDestino = input("País de destino: ")
    
    def __neg__(self):
        print(f"\n--- Datos del Crucero ---")
        print(f"Nombre: {self.__nombre}")
        print(f"País Origen: {self.__paisOrigen}")
        print(f"País Destino: {self.__paisDestino}")
        print(f"Número de Pasajeros: {self.__nroPasajeros}")
        print("\nPasajeros:")
        for i in range(self.__nroPasajeros):
            nombre = self.__pasajeros[i][0]
            nroHab = self.__pasajeros[i][1]
            costo = self.__pasajeros[i][2]
            print(f"  {i+1}. {nombre} - Hab: {nroHab} - Costo: {costo}")
    
    def __eq__(self, otro):
        total = 0
        for i in range(self.__nroPasajeros):
            total += int(self.__pasajeros[i][2])
        print(f"\nCosto total de pasajes del crucero '{self.__nombre}': {total}")
        return total
    
    def __add__(self, otro_crucero):
        if self.__nroPasajeros == otro_crucero.__nroPasajeros:
            print(f"\nLos cruceros '{self.__nombre}' y '{otro_crucero.__nombre}' tienen la misma cantidad de pasajeros ({self.__nroPasajeros})")
            return 1
        else:
            print(f"\nLos cruceros '{self.__nombre}' ({self.__nroPasajeros}) y '{otro_crucero.__nombre}' ({otro_crucero.__nroPasajeros}) tienen diferente cantidad de pasajeros")
            return 0
    
    def __sub__(self, otro):
        mujeres = 0
        hombres = 0
        for i in range(self.__nroPasajeros):
            genero = self.__pasajeros[i][3].upper()
            if genero == 'F' or genero == 'FEMENINO':
                mujeres += 1
            elif genero == 'M' or genero == 'MASCULINO':
                hombres += 1
        print(f"\nEn el crucero '{self.__nombre}':")
        print(f"  Mujeres: {mujeres}")
        print(f"  Hombres: {hombres}")
    
    def agregar_pasajero(self, nombre, nroHabitacion, costoPasaje, genero=""):
        self.__pasajeros.append([nombre, str(nroHabitacion), str(costoPasaje), genero])
        self.__nroPasajeros += 1


class Pasajero:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__genero = ""
    
    def __pos__(self):
        print("--- Ingreso de datos del Pasajero ---")
        self.__nombre = input("Nombre: ")
        self.__edad = int(input("Edad: "))
        self.__genero = input("Género (M/F): ")
    
    def __neg__(self):
        print(f"\n--- Datos del Pasajero ---")
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Género: {self.__genero}")

crucero1 = Crucero()
crucero2 = Crucero()

pasajero1 = Pasajero()
pasajero2 = Pasajero()
pasajero3 = Pasajero()
pasajero4 = Pasajero()
pasajero5 = Pasajero()

crucero1._Crucero__nombre = "Titanic II"
crucero1._Crucero__paisOrigen = "España"
crucero1._Crucero__paisDestino = "México"

crucero2._Crucero__nombre = "Nosequeponer"
crucero2._Crucero__paisOrigen = "Brasil"
crucero2._Crucero__paisDestino = "Argentina"

crucero1.agregar_pasajero("Juan Vargas", 502, 500, "M")
crucero1.agregar_pasajero("Martina Vasques", 603, 1000, "F")
crucero1.agregar_pasajero("Wilmer Montero", 401, 925, "M")

crucero2.agregar_pasajero("Ana Lopez", 201, 800, "F")
crucero2.agregar_pasajero("Pedro Gomez", 305, 750, "M")
crucero2.agregar_pasajero("Maria Torres", 410, 900, "F")

-crucero1
-crucero2

crucero1 == None

crucero1 + crucero2

crucero1 - None