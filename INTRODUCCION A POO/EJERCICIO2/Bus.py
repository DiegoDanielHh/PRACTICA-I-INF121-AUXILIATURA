class Bus:
    def __init__(self,cantPasajeros, asientos):
        self.cantPasajeros = cantPasajeros
        self.asientos = asientos
    def disponibles(self):
        dis = self.asientos - self.cantPasajeros
        print("Asientos disponibles: ",dis," asientos")
    
    def subirPasajero(self,nuevos):
        if (self.cantPasajeros + nuevos <= self.asientos):
            self.cantPasajeros = self.cantPasajeros + nuevos
            print(nuevos,"pasajeros subieron, el total es", self.cantPasajeros)
        else:
            print("no hay mas asientos para los",nuevos,"pasajeros") 
    
    def cobrar(self):
        total = 1.50 * self.cantPasajeros
        print("Se cobro a 1,50 y el total es", total, "Bs")
        
bus1=Bus(25, 32)
bus1.disponibles()
bus1.subirPasajero(2)
bus1.cobrar()
bus1.disponibles()