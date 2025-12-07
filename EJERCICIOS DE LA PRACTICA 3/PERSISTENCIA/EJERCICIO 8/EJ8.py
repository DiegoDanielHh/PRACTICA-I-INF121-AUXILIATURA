import json
from datetime import datetime

class Alimento:
    def __init__(self, nombre, fechaVencimiento, cantidad):
        self.nombre = nombre
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad

class ArchRefri:
    def __init__(self):
        self.alimentos = []
    
    def crear(self, alimento):
        self.alimentos.append(alimento)
    
    def modificar_nombre(self, nombre_actual, nombre_nuevo):
        for a in self.alimentos:
            if a.nombre == nombre_actual:
                a.nombre = nombre_nuevo
                return True
        return False
    
    def eliminar_nombre(self, nombre):
        self.alimentos = [a for a in self.alimentos if a.nombre != nombre]
    
    def guardar(self):
        with open('refri.json', 'w') as f:
            datos = [a.__dict__ for a in self.alimentos]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open('refri.json', 'r') as f:
                datos = json.load(f)
                self.alimentos = [Alimento(**d) for d in datos]
        except FileNotFoundError:
            self.alimentos = []
    
    def caducados(self, fecha_x):
        print(f"Alimentos caducados antes de {fecha_x}:")
        fecha_limite = datetime.strptime(fecha_x, "%Y-%m-%d")
        for a in self.alimentos:
            fecha_venc = datetime.strptime(a.fechaVencimiento, "%Y-%m-%d")
            if fecha_venc < fecha_limite:
                print(f"{a.nombre} - Vence: {a.fechaVencimiento}, Cantidad: {a.cantidad}")
    
    def eliminar_cantidad_cero(self):
        self.alimentos = [a for a in self.alimentos if a.cantidad > 0]
        print("Alimentos con 0 eliminados")
    
    def vencidos(self):
        print("Alimentos ya vencidos:")
        hoy = datetime.now()
        for a in self.alimentos:
            fecha_venc = datetime.strptime(a.fechaVencimiento, "%Y-%m-%d")
            if fecha_venc < hoy:
                print(f"{a.nombre} - Vence: {a.fechaVencimiento}, Cantidad: {a.cantidad}")
    
    def mayor_cantidad(self):
        if self.alimentos:
            max_cant = max(a.cantidad for a in self.alimentos)
            print(f"Alimento con mayor cantidad ({max_cant}):")
            for a in self.alimentos:
                if a.cantidad == max_cant:
                    print(f"{a.nombre} - Vence: {a.fechaVencimiento}")

refri = ArchRefri()

refri.crear(Alimento("Leche", "2024-12-10", 2))
refri.crear(Alimento("Yogurt", "2024-11-20", 0))
refri.crear(Alimento("Queso", "2025-01-15", 5))
refri.crear(Alimento("Jamón", "2024-12-01", 3))
refri.crear(Alimento("Mantequilla", "2025-02-20", 1))

refri.guardar()
refri.leer()

print("ALIMENTOS INICIALES")
for a in refri.alimentos:
    print(f"{a.nombre} - Vence: {a.fechaVencimiento}, Cantidad: {a.cantidad}")

print("\nMODIFICAR NOMBRE")
refri.modificar_nombre("Leche", "Leche Descremada")
print("Leche modificada a Leche Descremada")

print("\nELIMINAR POR NOMBRE")
refri.eliminar_nombre("Jamón")
print("Jamón eliminado")

print("\nCADUCADOS ANTES DE 2024-12-15")
refri.caducados("2024-12-15")

print("\nELIMINAR CANTIDAD 0")
refri.eliminar_cantidad_cero()

print("\nALIMENTOS VENCIDOS")
refri.vencidos()

print("\nMAYOR CANTIDAD")
refri.mayor_cantidad()

refri.guardar()