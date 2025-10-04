# a) Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def desplazarse(self):
        return f"{self.nombre} se está desplazando"

class Leon(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def desplazarse(self):
        return f"{self.nombre} está caminando"


class Pinguino(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def desplazarse(self):
        return f"{self.nombre} está nadando"


class Canguro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def desplazarse(self):
        return f"{self.nombre} está saltando"


animales = [Leon("Simba", 5), Pinguino("Skipper", 3),Canguro("Jack", 4)]
for i in animales:
    print(i.desplazarse())