import json

class Producto:
    def __init__(self, codigo=0, nombre="", precio=0.0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def convertir_a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio
        }

    def convertir_a_normal(self, datos):
        self.codigo = datos["codigo"]
        self.nombre = datos["nombre"]
        self.precio = datos["precio"]

    def mostrar(self):
        print(f"{self.codigo} {self.nombre} {self.precio}")


class ArchivoProducto:
    def __init__(self, n="productos.json"):
        self.nomA = n

    def crearArchivo(self):
        try:
            with open(self.nomA, "w") as f:
                json.dump([], f)
            print("Archivo creado")
        except Exception as e:
            print(f"{e}")

    def guardaProducto(self, p):
        try:
            with open(self.nomA, "r") as f:
                datos = json.load(f)
        except FileNotFoundError:
            datos = []

        datos.append(p.convertir_a_diccionario())

        try:
            with open(self.nomA, "w") as f:
                json.dump(datos, f)
            print("Guardado")
        except Exception as e:
            print(f"{e}")

    def buscaProducto(self, c):
        try:
            with open(self.nomA, "r") as f:
                datos = json.load(f)
            for d in datos:
                if d["codigo"] == c:
                    print(f'{d["codigo"]} {d["nombre"]} {d["precio"]}')
                    return
            print("No encontrado")
        except Exception as e:
            print(f"{e}")

    def promedioPrecios(self):
        try:
            with open(self.nomA, "r") as f:
                datos = json.load(f)
            if len(datos) == 0:
                print("Sin datos")
                return
            suma = 0
            for d in datos:
                suma += d["precio"]
            promedio = suma / len(datos)
            print(f"{promedio}")
        except Exception as e:
            print(f"{e}")

    def productoMasCaro(self):
        try:
            with open(self.nomA, "r") as f:
                datos = json.load(f)
            if len(datos) == 0:
                print("Sin datos")
                return
            caro = datos[0]
            for d in datos:
                if d["precio"] > caro["precio"]:
                    caro = d
            print(f'{caro["codigo"]} {caro["nombre"]} {caro["precio"]}')
        except Exception as e:
            print(f"{e}")

p1 = Producto(101, "Laptop", 4500.0)
p2 = Producto(102, "Mouse", 120.0)
p3 = Producto(103, "Monitor", 980.0)

archivo = ArchivoProducto("productos.json")
archivo.crearArchivo()

archivo.guardaProducto(p1)
archivo.guardaProducto(p2)
archivo.guardaProducto(p3)

archivo.buscaProducto(102)
archivo.promedioPrecios()
archivo.productoMasCaro()
