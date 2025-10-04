from multimethod import multimethod

class Parada:
    def __init__(self, nombreP="SinNombre"):
        self.admins = [""] * 10
        self.autos = [["", ""] for _ in range(10)]
        self.__nombreP = nombreP

    def mostrar(self):
        print(f"Parada: {self.__nombreP}")
        
        print("\nAdministradores:")
        tiene_admins = False
        for i in range(10):
            if self.admins[i] != "":
                print(f"  {i+1}. {self.admins[i]}")
                tiene_admins = True
        if not tiene_admins:
            print("  (ninguno)")
        
        print("\nAutos:")
        tiene_autos = False
        for i in range(10):
            if self.autos[i][0] != "":
                modelo = self.autos[i][0]
                conductor = self.autos[i][1]
                print(f"  {i+1}. Modelo: {modelo}, Conductor: {conductor}")
                tiene_autos = True
        if not tiene_autos:
            print("  (ninguno)")

    @multimethod
    def adicionar(self, admin: str):
        for i in range(10):
            if self.admins[i] == "":
                self.admins[i] = admin
                break
        else:
            print("No se pueden añadir más administradores.")

    @multimethod
    def adicionar(self, x: str, y: str, z: str):
        for i in range(10):
            if self.autos[i][0] == "":
                self.autos[i][0] = x 
                self.autos[i][1] = y 
                break
        else:
            print("No se pueden añadir más autos.")


p = Parada("Parada principl")

p.adicionar("Pedro")                        
p.adicionar("Juanito")    
p.adicionar("Toyota", "Carlos", "123ABC")
p.adicionar("Audi", "Antonio", "987HDH")
p.mostrar()