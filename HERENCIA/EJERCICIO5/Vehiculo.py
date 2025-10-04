class Vehiculo:
    def __init__(self, conductor, placa, id):
        self._conductor = conductor 
        self._placa = placa         
        self._id = id               

class Bus(Vehiculo):
    def __init__(self, conductor, placa, id, capacidad, sindicato):
        super().__init__(conductor, placa, id)
        self.__capacidad = capacidad      
        self.__sindicato = sindicato     

class Auto(Vehiculo):
    def __init__(self, conductor, placa, id, caballosFuerza, descapotable):
        super().__init__(conductor, placa, id)
        self.__caballosFuerza = caballosFuerza    
        self.__descapotable = descapotable        

class Moto(Vehiculo):
    def __init__(self, conductor, placa, id, cilindrada, casco):
        super().__init__(conductor, placa, id)
        self.__cilindrada = cilindrada    
        self.__casco = casco              


bus1 = Bus("Juan Pérez", "ABC-123", 1, 50, "Sindicato Norte")
auto1 = Auto("María López", "XYZ-789", 2, 150, True)
moto1 = Moto("Carlos Ruiz", "MOT-456", 3, 250, True)

print(f"Bus - Conductor: {bus1._conductor}, Placa: {bus1._placa}")
print(f"Auto - Conductor: {auto1._conductor}, Placa: {auto1._placa}")
print(f"Moto - Conductor: {moto1._conductor}, Placa: {moto1._placa}")

def cambiar_conductor(vehiculo, nuevo_conductor):
    vehiculo._conductor = nuevo_conductor
    print(f"\nConductor cambiado a: {nuevo_conductor}")

print(f"Conductor actual del bus: {bus1._conductor}")
cambiar_conductor(bus1, "Pedro Gonzales")
print(f"Nuevo conductor del bus: {bus1._conductor}")