# Excepciones personalizadas
class ProductoNoEncontradoException(Exception):
    pass

class StockInsuficienteException(Exception):
    pass

class CodigoDuplicadoException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Codigo:{self.codigo} Nombre:{self.nombre} Precio:{self.precio}Bs Stock:{self.stock}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, codigo, nombre, precio, stock):
        for p in self.productos:
            if p.codigo == codigo:
                raise CodigoDuplicadoException(f"El código ya existe")
        if precio < 0 or stock < 0:
            raise ValorInvalidoException("el precio y stock no pueden ser negativos")

        nuevo = Producto(codigo, nombre, precio, stock)
        self.productos.append(nuevo)

    def buscar_producto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        raise ProductoNoEncontradoException(f"Producto no encontrado")

    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto.stock >= cantidad:
            producto.stock -= cantidad
        else:
            raise StockInsuficienteException(
                f"No hay stock suficiente"
            )

    def mostrar_inventario(self):
        print("Inventario:")
        for p in self.productos:
            print(p)

inv = Inventario()

try:
    inv.agregar_producto("P001", "Laptop", 1500, 10)
    inv.agregar_producto("P002", "Mouse", 20, 50)
    inv.agregar_producto("P003", "Teclado", 30, 30)
except (CodigoDuplicadoException, ValorInvalidoException) as e:
    print("Error al agregar producto:", e)

inv.mostrar_inventario()
try:
    print("\nBuscando producto P002:")
    print(inv.buscar_producto("P002"))
except ProductoNoEncontradoException as e:
    print("Error:", e)

try:
    print("\nVendiendo 5 laptops")
    inv.vender_producto("P001", 5)
    print(inv.buscar_producto("P001"))
except (ProductoNoEncontradoException, StockInsuficienteException) as e:
    print("Error en venta:", e)

try:
    print("\nVendiendo 50 teclados")
    inv.vender_producto("P003", 50)
except StockInsuficienteException as e:
    print("Error en venta:", e)

try:
    print("\nBuscando producto P999:")
    print(inv.buscar_producto("P999"))
except ProductoNoEncontradoException as e:
    print("Error:", e)
