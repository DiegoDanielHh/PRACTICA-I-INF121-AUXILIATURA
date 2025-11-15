class Producto:
    def __init__(self, precio, nombre):
        self.precio = precio
        self.nombre = nombre
    
    def cambiarNombre(self, nom):
        self.nombre = nom
    
    def reducirPrecio(self):
        self.precio = self.precio * 0.9
        return self.precio

class Inventario:
    def __init__(self, ubicacion, capacidadMax):
        self.ubicacion = ubicacion
        self.capacidadMax = capacidadMax
        self.productos = []
    
    def agregarMed(self, med):
        self.productos.append(med)
    
    def mostrar(self):
        print(f"INVENTARIO: ")
        print(f"Ubicacion: {self.ubicacion}")
        print(f"Capacidad máxima: {self.capacidadMax}")
        print(f"Productos: {len(self.productos)}")
        for prod in self.productos:
            print(f"Nombre: {prod.nombre}, Precio: {prod.precio}Bs")

class Medicamento:
    def __init__(self, nombre, fechaVencimiento, precio):
        self.nombre = nombre
        self.fechaVencimiento = fechaVencimiento
        self.precio = precio
    
    def veriVencimiento(self):
        fechaHoy = "2025-11-02"
        if self.fechaVencimiento < fechaHoy:
            return True
        else:
            return False
    
    def monto(self, compraron):
        total = self.precio * compraron
        return total

class Registro:
    def __init__(self, tipo, responsable):
        self.tipo = tipo
        self.responsable = responsable
    
    def verificarVenta(self):
        if self.tipo.lower() == "venta":
            return True
        else:
            return False
    
    def verificarCompra(self):
        if self.tipo.lower() == "compra":
            return True
        else:
            return False

class Farmacia:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.medicamentos = []
        self.registros = []
    
    def venderMed(self, nombre, cantidad):
        print(f"Se vendió el medicamento: {nombre} con cantidad: {cantidad}")
    
    def generarReporte(self):
        print(f"REPORTE")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Total de registros: {len(self.registros)}")
        contador = 1
        for reg in self.registros:
            print(f"Registro {contador}:")
            print(f"Tipo: {reg.tipo}")
            print(f"Responsable: {reg.responsable}")
            contador += 1

producto1 = Producto(150, "Jarabe")
producto2 = Producto(200, "Tabletas")

medicamento1 = Medicamento("Paracetamol", "2025-12-31", 50)
medicamento2 = Medicamento("Ibuprofeno", "2024-06-30", 75)

inventario1 = Inventario("Bodega A", 500)
inventario1.agregarMed(producto1)
inventario1.agregarMed(producto2)
inventario1.agregarMed(medicamento1)
inventario1.agregarMed(medicamento2)

farmacia1 = Farmacia("Farmacia Farmacorp", "Av. Arce 123")
farmacia1.inventario = inventario1
farmacia1.medicamentos.append(medicamento1)
farmacia1.medicamentos.append(medicamento2)

registro1 = Registro("Venta", "Juan Pérez")
registro2 = Registro("Compra", "María López")
farmacia1.registros.append(registro1)
farmacia1.registros.append(registro2)
inventario1.mostrar()

print(f"{medicamento1.nombre} esta vencido: {medicamento1.veriVencimiento()}")
print(f"{medicamento2.nombre} está vencido: {medicamento2.veriVencimiento()}")

print(f"Monto por 10 unidades de {medicamento1.nombre}: {medicamento1.monto(10)}Bs")

farmacia1.venderMed("Paracetamol", 5)
farmacia1.generarReporte()