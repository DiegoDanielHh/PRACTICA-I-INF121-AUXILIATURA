class Cafeteria:
    def __init__(self, nombre, menu):
        self.__nombre = nombre
        self.__menu = menu 

    def __del__(self):
        print(f"Cafetería: {self.__nombre} eliminada")

    def getNombre(self):
        return self.__nombre
    
    def getMenu(self):
        return self.__menu

    def setNombre(self, otro):
        self.__nombre = otro
    
    def setMenu(self, otro):
        self.__menu = otro

class Producto:
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado

    def __del__(self):
        print(f"Producto: {self.__nombre} eliminado")

    def getNombre(self):
        return self.__nombre
    
    def getEstado(self):
        return self.__estado

    def setNombre(self, otro):
        self.__nombre = otro
    
    def setEstado(self, otro):
        self.__estado = otro

print("CLASE CAFETERIA")
menu = ["Espresso", "Americano", "Latte"]
cafeteria1 = Cafeteria("El rincón del cafe", menu)

print("Nombre:", cafeteria1.getNombre())
print("Menú:", cafeteria1.getMenu())

print("CLASE PRODUCTO")
producto1 = Producto("Espresso", "registrado")

print("Nombre:", producto1.getNombre())
print("Estado:", producto1.getEstado())
