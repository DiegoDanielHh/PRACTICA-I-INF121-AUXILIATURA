import json

class Estudiante:
    def __init__(self, ru, nombre, paterno, materno, edad):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad

    def convertir_a_diccionario(self):
        return {
            "ru": self.ru,
            "nombre": self.nombre,
            "paterno": self.paterno,
            "materno": self.materno,
            "edad": self.edad
        }

    def convertir_a_normal(self, datos):
        self.ru = datos["ru"]
        self.nombre = datos["nombre"]
        self.paterno = datos["paterno"]
        self.materno = datos["materno"]
        self.edad = datos["edad"]

    def mostrar(self):
        print(self.ru, self.nombre, self.paterno, self.materno, self.edad)


class Nota:
    def __init__(self, materno, notaFinal, estudiante):
        self.materno = materno
        self.notaFinal = notaFinal
        self.estudiante = estudiante

    def convertir_a_diccionario(self):
        return {
            "materno": self.materno,
            "notaFinal": self.notaFinal,
            "estudiante": self.estudiante.convertir_a_diccionario()
        }

    def convertir_a_normal(self, datos):
        self.materno = datos["materno"]
        self.notaFinal = datos["notaFinal"]
        est = Estudiante(
            datos["estudiante"]["ru"],
            datos["estudiante"]["nombre"],
            datos["estudiante"]["paterno"],
            datos["estudiante"]["materno"],
            datos["estudiante"]["edad"]
        )
        self.estudiante = est

    def mostrar(self):
        print(self.materno, self.notaFinal)
        self.estudiante.mostrar()


class ArchiNota:
    def __init__(self, nombreArchi):
        self.nombreArchi = nombreArchi

    def agregarNotas(self, lista):
        try:
            datos = []
            for n in lista:
                datos.append(n.convertir_a_diccionario())
            with open(self.nombreArchi, "w") as f:
                json.dump(datos, f)
            print("Guardado")
        except Exception as e:
            print(e)

    def promedioNotas(self):
        try:
            with open(self.nombreArchi, "r") as f:
                datos = json.load(f)
            if len(datos) == 0:
                print("Sin datos")
                return
            suma = 0
            for d in datos:
                suma += d["notaFinal"]
            promedio = suma / len(datos)
            print(promedio)
        except Exception as e:
            print(e)

    def mejoresNotas(self):
        try:
            with open(self.nombreArchi, "r") as f:
                datos = json.load(f)
            if len(datos) == 0:
                print("Sin datos")
                return
            mejor = max(d["notaFinal"] for d in datos)
            for d in datos:
                if d["notaFinal"] == mejor:
                    print(d["materno"], d["notaFinal"], d["estudiante"]["nombre"])
        except Exception as e:
            print(e)

    def eliminarPorMateria(self, materia):
        try:
            with open(self.nombreArchi, "r") as f:
                datos = json.load(f)
            nueva = []
            for d in datos:
                if d["materno"] != materia:
                    nueva.append(d)
            with open(self.nombreArchi, "w") as f:
                json.dump(nueva, f)
            print("Eliminado")
        except Exception as e:
            print(e)

e1 = Estudiante(1, "Ana", "Perez", "Matematicas", 20)
e2 = Estudiante(2, "Luis", "Gomez", "Fisica", 21)
e3 = Estudiante(3, "Sofia", "Lopez", "Matematicas", 22)

n1 = Nota("Matematicas", 85.0, e1)
n2 = Nota("Fisica", 92.0, e2)
n3 = Nota("Matematicas", 92.0, e3)

archivo = ArchiNota("notas.json")
archivo.agregarNotas([n1, n2, n3])

archivo.promedioNotas()
archivo.mejoresNotas()
archivo.eliminarPorMateria("Matematicas")
