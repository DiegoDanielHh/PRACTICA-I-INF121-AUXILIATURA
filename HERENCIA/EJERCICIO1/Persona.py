class Persona:
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self. ci = ci
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, ci: {self.ci}"
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, ci, nroCompra, idCliente):
        super().__init__(nombre, apellido, ci)
        self.nroCompra = nroCompra
        self.idCliente = idCliente
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, ci: {self.ci}, NroCompra: {self.nroCompra}, ID: {self.idCliente}"
    

class Jefe(Persona):
    def __init__(self, nombre, apellido, ci, sucursal, tipo):
        super().__init__(nombre, apellido, ci)
        self.sucursal = sucursal
        self.tipo = tipo
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, ci: {self.ci}, sucursal: {self.sucursal}, tipo: {self.tipo}"
    

pe = Persona("juan", "perez", 1234566)
print(pe)

cl = Cliente("pedro","picapiedra", 12312312, 23, 191991)
print(cl)

je = Jefe("pablo", "perez", 8776655, "Sucursal Centro", "galeria")
print(je)