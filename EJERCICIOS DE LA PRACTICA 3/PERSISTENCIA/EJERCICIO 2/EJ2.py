import json

class Trabajador:
    def __init__(self, nombre="", carnet=0, salario=0.0):
        self.__nombre = nombre
        self.__carnet = carnet
        self.__salario = salario

    def convertir_a_diccionario(self):
        return {
            "nombre": self.__nombre,
            "carnet": self.__carnet,
            "salario": self.__salario
        }

    def convertir_a_normal(self, datos):
        self.__nombre = datos["nombre"]
        self.__carnet = datos["carnet"]
        self.__salario = datos["salario"]

    def aumentar_salario(self, aumento):
        self.__salario += aumento

    def obtener_salario(self):
        return self.__salario

    def mostrar(self):
        print(f"{self.__nombre} {self.__carnet} {self.__salario}")


class ArchivoTrabajador:
    def __init__(self):
        self.__nombreArch = "trabajadores.json"

    def crearArchivo(self):
        try:
            with open(self.__nombreArch, "w") as f:
                json.dump([], f)
            print("Archivo creado")
        except Exception as e:
            print(e)

    def guardarTrabajador(self, t):
        try:
            with open(self.__nombreArch, "r") as f:
                datos = json.load(f)
        except FileNotFoundError:
            datos = []

        datos.append(t.convertir_a_diccionario())

        try:
            with open(self.__nombreArch, "w") as f:
                json.dump(datos, f)
            print("Guardado")
        except Exception as e:
            print(e)

    def aumentaSalario(self, a, t):
        t.aumentar_salario(a)
        print("Salario aumentado")

    def buscarMayorSalario(self):
        try:
            with open(self.__nombreArch, "r") as f:
                datos = json.load(f)
            mayor = None
            for d in datos:
                if mayor is None or d["salario"] > mayor["salario"]:
                    mayor = d
            if mayor:
                print(f'{mayor["nombre"]} {mayor["carnet"]} {mayor["salario"]}')
        except Exception as e:
            print(e)

    def ordenarPorSalario(self):
        try:
            with open(self.__nombreArch, "r") as f:
                datos = json.load(f)
            n = len(datos)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if datos[j]["salario"] > datos[j + 1]["salario"]:
                        temp = datos[j]
                        datos[j] = datos[j + 1]
                        datos[j + 1] = temp
            for d in datos:
                print(f'{d["nombre"]} {d["carnet"]} {d["salario"]}')
        except Exception as e:
            print(e)


t1 = Trabajador("Ana", 123, 2500.0)
t2 = Trabajador("Luis", 456, 3200.0)
t3 = Trabajador("Sofia", 789, 2800.0)

archivo = ArchivoTrabajador()
archivo.crearArchivo()

archivo.guardarTrabajador(t1)
archivo.guardarTrabajador(t2)
archivo.guardarTrabajador(t3)

archivo.aumentaSalario(500, t1)
archivo.guardarTrabajador(t1)

archivo.buscarMayorSalario()
archivo.ordenarPorSalario()
