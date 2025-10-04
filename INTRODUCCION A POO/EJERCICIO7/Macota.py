class Mascota:
    def __init__(self,nombre, tipo, energia):
        self.__nombre =  nombre
        self.__tipo = tipo
        self.__energia = energia
    
    def getEnergia(self):
        return self.__energia
    
    def alimentar(self):

        if self.__energia + 20 <= 100:
            self.__energia = self.__energia +20
            return f"Se alimentó a la mascota, energía actual: {self.getEnergia()}"
        else:
            return f"se alcanzó el limite"
        
    def jugar(self):
        if self.__energia - 15 >= 0:
            self.__energia = self.__energia - 15
            return f"La mascota comenzó a jugar, energía actual: {self.getEnergia()}"
            
        else:
            return f"energia insuficiente"

print("MASCOTA 1")
mas1 = Mascota("Doggy", "perro", 75)
print(f"Energia: {mas1.getEnergia()}")
print(mas1.jugar())
print(mas1.alimentar())
print("MASCOTA 2")
mas2 = Mascota("Pelusa", "gato", 60)
print(f"Energia: {mas2.getEnergia()}")
print(mas2.alimentar())
print(mas2.jugar())