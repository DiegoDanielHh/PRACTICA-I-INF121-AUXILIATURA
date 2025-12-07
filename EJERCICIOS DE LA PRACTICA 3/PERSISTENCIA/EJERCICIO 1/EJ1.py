import json

class Charango:
    def __init__(self, material="", nroCuerdas=0, cuerdas=None):
        if cuerdas is None:
            cuerdas = []
        self.material = material
        self.nroCuerdas = nroCuerdas
        self.cuerdas = cuerdas

    def convertir_a_diccionario(self):
        return {
            "material": self.material,
            "nroCuerdas": self.nroCuerdas,
            "cuerdas": self.cuerdas
        }

    def cargar_desde_diccionario(self, datos):
        self.material = datos["material"]
        self.nroCuerdas = datos["nroCuerdas"]
        self.cuerdas = datos["cuerdas"]

    @staticmethod
    def guardar_charangos(lista, archivo):
        try:
            datos = []
            for c in lista:
                datos.append(c.convertir_a_diccionario())
            with open(archivo, "w") as f:
                json.dump(datos, f)
            print("Archivo guardado correctamente.")
        except Exception as e:
            print("Error al guardar:", e)

    @staticmethod
    def cargar_charangos(archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
            lista = []
            for d in datos:
                c = Charango()
                c.cargar_desde_diccionario(d)
                lista.append(c)
            print("Archivo cargado correctamente.")
            return lista
        except FileNotFoundError:
            print("El archivo no existe.")
            return []
        except Exception as e:
            print("Error al cargar:", e)
            return []

    @staticmethod
    def eliminar_charangos_defectuosos(lista):
        nueva_lista = []
        for c in lista:
            if c.cuerdas.count(False) <= 6:
                nueva_lista.append(c)
        return nueva_lista

    @staticmethod
    def listar_por_material(lista, material):
        resultado = []
        for c in lista:
            if c.material == material:
                resultado.append(c)
        return resultado

    @staticmethod
    def buscar_con_10_cuerdas(lista):
        resultado = []
        for c in lista:
            if c.nroCuerdas == 10:
                resultado.append(c)
        return resultado

    @staticmethod
    def ordenar_por_material(lista):
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if lista[j].material > lista[j + 1].material:
                    temp = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temp
        return lista


charangos = [
    Charango("madera", 10, [True]*10),
    Charango("plastico", 8, [False]*7 + [True]),
    Charango("madera", 10, [True]*9 + [False]),
    Charango("metal", 10, [True]*10)
]

Charango.guardar_charangos(charangos, "charangos.json")
cargados = Charango.cargar_charangos("charangos.json")

filtrados = Charango.eliminar_charangos_defectuosos(cargados)
madera = Charango.listar_por_material(filtrados, "madera")
diez_cuerdas = Charango.buscar_con_10_cuerdas(filtrados)
ordenados = Charango.ordenar_por_material(filtrados)

print("Charangos válidos:", len(filtrados))
print("Hechos de madera:", len(madera))
print("Con 10 cuerdas:", len(diez_cuerdas))

print("Materiales ordenados:")
for c in ordenados:
    print(c.material)
