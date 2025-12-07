import json

class Medicamento:
    def __init__(self):
        self.__nombre = ""
        self.__codMedicamento = 0
        self.__tipo = ""
        self.__precio = 0.0

    def leer(self, datos):
        self.__nombre = datos["nombre"]
        self.__codMedicamento = datos["codMedicamento"]
        self.__tipo = datos["tipo"]
        self.__precio = datos["precio"]

    def mostrar(self):
        print(self.__nombre, self.__codMedicamento, self.__tipo, self.__precio)

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio

    def getNombre(self):
        return self.__nombre


class Farmacia:
    def __init__(self):
        self.__nombreFarmacia = ""
        self.__sucursal = 0
        self.__direccion = ""
        self.__nroMedicamentos = 0
        self.__m = [None] * 100

    def leer(self, datos):
        self.__nombreFarmacia = datos["nombreFarmacia"]
        self.__sucursal = datos["sucursal"]
        self.__direccion = datos["direccion"]
        meds = datos.get("medicamentos", [])
        self.__nroMedicamentos = len(meds)
        for i, med_data in enumerate(meds):
            med = Medicamento()
            med.leer(med_data)
            self.__m[i] = med

    def mostrar(self):
        print(self.__nombreFarmacia, self.__sucursal, self.__direccion, self.__nroMedicamentos)
        for i in range(self.__nroMedicamentos):
            self.__m[i].mostrar()

    def getDireccion(self):
        return self.__direccion

    def getSucursal(self):
        return self.__sucursal

    def mostrarMedicamentos(self, x):
        for i in range(self.__nroMedicamentos):
            if self.__m[i].getTipo() == x:
                self.__m[i].mostrar()

    def buscaMedicamento(self, x):
        for i in range(self.__nroMedicamentos):
            if self.__m[i].getNombre() == x:
                return True
        return False

    def getMedicamentos(self):
        return self.__m[:self.__nroMedicamentos]

    def getNombreFarmacia(self):
        return self.__nombreFarmacia


class ArchFarmacia:
    def __init__(self, na):
        self.__na = na
        self.__lista = []

    def crearArchivo(self):
        self.__lista = []
        with open(self.__na, "w") as f:
            json.dump([], f)
        print("Archivo creado")

    def adicionar(self, farmacia):
        self.__lista.append(farmacia)
        datos = []
        for f in self.__lista:
            datos.append({
                "nombreFarmacia": f.getNombreFarmacia(),
                "sucursal": f.getSucursal(),
                "direccion": f.getDireccion(),
                "medicamentos": [
                    {
                        "nombre": med.getNombre(),
                        "codMedicamento": med._Medicamento__codMedicamento,
                        "tipo": med.getTipo(),
                        "precio": med.getPrecio()
                    }
                    for med in f.getMedicamentos()
                ]
            })
        with open(self.__na, "w") as f:
            json.dump(datos, f)
        print("Adicionado")

    def leer(self):
        with open(self.__na, "r") as f:
            datos = json.load(f)
        self.__lista = []
        for farm_data in datos:
            f = Farmacia()
            f.leer(farm_data)
            self.__lista.append(f)

    def listar(self):
        for f in self.__lista:
            f.mostrar()

    def mostrarMedicamentosResfrios(self):
        for f in self.__lista:
            for med in f.getMedicamentos():
                if med.getTipo() == "resfrio":
                    med.mostrar()

    def precioMedicamentoTos(self):
        total = 0
        for f in self.__lista:
            for med in f.getMedicamentos():
                if med.getTipo() == "tos":
                    total += med.getPrecio()
        return total

    def mostrarMedicamentosMenorTos(self):
        for f in self.__lista:
            for med in f.getMedicamentos():
                if med.getTipo() == "tos" and med.getPrecio() < 50:
                    med.mostrar()

farmacia_data = {
    "nombreFarmacia": "Farmacia Central",
    "sucursal": 1,
    "direccion": "Av. Principal",
    "medicamentos": [
        {"nombre": "Tapsin", "codMedicamento": 101, "tipo": "resfrio", "precio": 25.0},
        {"nombre": "Jarabe", "codMedicamento": 102, "tipo": "tos", "precio": 60.0},
        {"nombre": "Pastilla", "codMedicamento": 103, "tipo": "tos", "precio": 40.0}
    ]
}

f1 = Farmacia()
f1.leer(farmacia_data)

archivo = ArchFarmacia("farmacias.json")
archivo.crearArchivo()
archivo.adicionar(f1)

archivo.leer()
archivo.listar()
archivo.mostrarMedicamentosResfrios()
print("Precio total medicamentos para la tos:", archivo.precioMedicamentoTos())
archivo.mostrarMedicamentosMenorTos()
