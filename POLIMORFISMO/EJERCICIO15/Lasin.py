from multimethod import multimethod

class Ordenador:
    def __init__(self, codigoSerial="", numero=0, memoriaRAM=0, procesador="", estado=""):
        self.__codigoSerial = codigoSerial
        self.__numero = numero
        self.__memoriaRAM = memoriaRAM
        self.__procesador = procesador
        self.__estado = estado
    
    def get_codigo_serial(self):
        return self.__codigoSerial
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado
    
    def get_memoria_ram(self):
        return self.__memoriaRAM
    
    def mostrar(self):
        print(f"Código: {self.__codigoSerial}, Número: {self.__numero}, RAM: {self.__memoriaRAM}GB, Procesador: {self.__procesador}, Estado: {self.__estado}")

class Laboratorio:
    def __init__(self, nombre="", capacidad=0):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__cantidadOrdenadores = 0
        self.__codigosSeriales = []
    
    def agregar_ordenador(self, ordenador):
        self.__codigosSeriales.append(ordenador.get_codigo_serial())
        self.__cantidadOrdenadores += 1
    
    def get_nombre(self):
        return self.__nombre
    
    def get_codigos_seriales(self):
        return self.__codigosSeriales
    
    @multimethod
    def informacion(self, estado: str, ordenadores: list):
        print(f"\nOrdenadores con estado '{estado}':")
        for ord in ordenadores:
            if ord.get_estado() == estado:
                ord.mostrar()
    
    @multimethod
    def informacion(self, nombreLab: str, ordenadores: list):
        print(f"\nOrdenadores del laboratorio '{nombreLab}':")
        for ord in ordenadores:
            if ord.get_codigo_serial() in self.__codigosSeriales:
                ord.mostrar()
    
    @multimethod
    def informacion(self, ram: int, ordenadores: list):
        print(f"\nOrdenadores con más de {ram}GB de RAM:")
        for ord in ordenadores:
            if ord.get_memoria_ram() > ram:
                ord.mostrar()


lab1 = Laboratorio("Lasin 1", 20)
lab2 = Laboratorio("Lasin 2", 25)

ord1 = Ordenador("SN001", 1, 8, "Intel i5", "activo")
ord2 = Ordenador("SN002", 2, 16, "Intel i7", "inactivo")
ord3 = Ordenador("SN003", 3, 4, "AMD Ryzen 3", "activo")
ord4 = Ordenador("SN004", 4, 16, "Intel i9", "activo")
ord5 = Ordenador("SN005", 5, 8, "AMD Ryzen 5", "inactivo")
ord6 = Ordenador("SN006", 6, 32, "Intel i7", "activo")

lab1.agregar_ordenador(ord1)
lab1.agregar_ordenador(ord2)
lab1.agregar_ordenador(ord3)

lab2.agregar_ordenador(ord4)
lab2.agregar_ordenador(ord5)
lab2.agregar_ordenador(ord6)

todos_ordenadores = [ord1, ord2, ord3, ord4, ord5, ord6]

lab1.informacion("activo", todos_ordenadores)
lab1.informacion("Lasin 1", todos_ordenadores)
lab1.informacion(8, todos_ordenadores)

print(f"\nEstado antes del traslado:")
print(f"Lab1: Estado de ord1 = {ord1.get_estado()}")
print(f"Lab1: Estado de ord2 = {ord2.get_estado()}")

ord1.set_estado("inactivo")
ord2.set_estado("inactivo")

lab1._Laboratorio__codigosSeriales.remove(ord1.get_codigo_serial())
lab1._Laboratorio__codigosSeriales.remove(ord2.get_codigo_serial())
lab1._Laboratorio__cantidadOrdenadores -= 2

lab2.agregar_ordenador(ord1)
lab2.agregar_ordenador(ord2)

ord1.set_estado("activo")
ord2.set_estado("activo")

print(f"\nEstado después del traslado:")
print(f"Lab2: Estado de ord1 = {ord1.get_estado()}")
print(f"Lab2: Estado de ord2 = {ord2.get_estado()}")

print("\nOrdenadores en Lasin 1:")
lab1.informacion("Lasin 1", todos_ordenadores)

print("\nOrdenadores en Lasin 2:")
lab2.informacion("Lasin 2", todos_ordenadores)