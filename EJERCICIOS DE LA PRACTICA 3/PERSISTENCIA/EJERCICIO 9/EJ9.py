import json

class Animal:
    def __init__(self, especie, nombre, cantidad):
        self.__especie = especie
        self.__nombre = nombre
        self.__cantidad = cantidad
    
    def getEspecie(self):
        return self.__especie
    
    def getNombre(self):
        return self.__nombre
    
    def getCantidad(self):
        return self.__cantidad
    
    def toDict(self):
        return {"especie": self.__especie, "nombre": self.__nombre, "cantidad": self.__cantidad}

class Zoologico:
    def __init__(self, id, nombre, nroAnimales):
        self.__id = id
        self.__nombre = nombre
        self.__nroAnimales = nroAnimales
        self.__animales = []
    
    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getAnimales(self):
        return self.__animales
    
    def agregarAnimal(self, animal):
        if len(self.__animales) < 30:
            self.__animales.append(animal)
            self.__nroAnimales = len(self.__animales)
    
    def limpiarAnimales(self):
        self.__animales = []
        self.__nroAnimales = 0
    
    def toDict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "nroAnimales": self.__nroAnimales,
            "animales": [a.toDict() for a in self.__animales]
        }

class ArchZoo:
    def __init__(self):
        self.__zoologicos = []
    
    def crear(self, zoologico):
        self.__zoologicos.append(zoologico)
    
    def modificar(self, id, nuevo_nombre):
        for z in self.__zoologicos:
            if z.getId() == id:
                z.setNombre(nuevo_nombre)
                return True
        return False
    
    def eliminar(self, id):
        self.__zoologicos = [z for z in self.__zoologicos if z.getId() != id]
    
    def guardar(self):
        with open("zoologicos.json", "w") as f:
            datos = [z.toDict() for z in self.__zoologicos]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("zoologicos.json", "r") as f:
                datos = json.load(f)
                self.__zoologicos = []
                for d in datos:
                    z = Zoologico(d["id"], d["nombre"], d["nroAnimales"])
                    for a in d["animales"]:
                        z.agregarAnimal(Animal(a["especie"], a["nombre"], a["cantidad"]))
                    self.__zoologicos.append(z)
        except FileNotFoundError:
            self.__zoologicos = []
    
    def mayorVariedad(self):
        print("Zoológicos con mayor variedad de animales:")
        for z in self.__zoologicos:
            especies = set(a.getEspecie() for a in z.getAnimales())
            print(f"{z.getNombre()} - {len(especies)} especies diferentes")
    
    def vaciosEliminar(self):
        print("Zoológicos vacios eliminados:")
        vacios = [z.getNombre() for z in self.__zoologicos if len(z.getAnimales()) == 0]
        for nombre in vacios:
            print(f"- {nombre}")
        self.__zoologicos = [z for z in self.__zoologicos if len(z.getAnimales()) > 0]
    
    def animalesEspecie(self, especie):
        print(f"Animales de la especie {especie}:")
        for z in self.__zoologicos:
            for a in z.getAnimales():
                if a.getEspecie() == especie:
                    print(f"{a.getNombre()} en {z.getNombre()} - Cantidad: {a.getCantidad()}")
    
    def moverAnimales(self, id_origen, id_destino):
        zoo_origen = None
        zoo_destino = None
        
        for z in self.__zoologicos:
            if z.getId() == id_origen:
                zoo_origen = z
            if z.getId() == id_destino:
                zoo_destino = z
        
        if zoo_origen and zoo_destino:
            for animal in zoo_origen.getAnimales():
                zoo_destino.agregarAnimal(animal)
            zoo_origen.limpiarAnimales()
            print(f"Animales movidos de {zoo_origen.getNombre()} a {zoo_destino.getNombre()}")

arch = ArchZoo()

leon1 = Animal("León", "Simba", 3)
tigre1 = Animal("Tigre", "Raja", 2)
leon2 = Animal("León", "Nala", 2)

zoo1 = Zoologico(1, "Zoo Central", 0)
zoo1.agregarAnimal(leon1)
zoo1.agregarAnimal(tigre1)

zoo2 = Zoologico(2, "Zoo Norte", 0)
zoo2.agregarAnimal(leon2)

zoo3 = Zoologico(3, "Zoo Vacío", 0)

arch.crear(zoo1)
arch.crear(zoo2)
arch.crear(zoo3)

arch.guardar()
arch.leer()

print("Zoológicos iniciales")
for z in arch._ArchZoo__zoologicos:
    print(f"{z.getNombre()} (ID: {z.getId()})")
    for a in z.getAnimales():
        print(f"{a.getNombre()} ({a.getEspecie()}): {a.getCantidad()}")
print("\nmodificar zoológico")
arch.modificar(1, "Zoo Central Renovado")
print("Zoo 1 modificado")

print("\nmayor variedad")
arch.mayorVariedad()

print("\nzoológicos vacíos")
arch.vaciosEliminar()

print("\nanimales de especie león")
arch.animalesEspecie("León")

print("\nmover animales")
arch.moverAnimales(2, 1)
print("\nzoológicos finales")
for z in arch._ArchZoo__zoologicos:
    print(f"{z.getNombre()} (ID: {z.getId()})")
    for a in z.getAnimales():
        print(f"{a.getNombre()} ({a.getEspecie()}): {a.getCantidad()}")
arch.guardar()