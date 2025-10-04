class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            print("Se vendieron ",cantidad, self.nombre, "Quedan: ",self.stock, self.nombre)
        else:
            print("No hay suficiente producto")
    
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print("se reabastecieron ", cantidad, self.nombre, "quedan: ",self.stock, self.nombre)
    
o1 = Producto("galletas", 2, 40)
print("El stock es: ",o1.stock)
o1.vender(5)
o1.reabastecer(8)