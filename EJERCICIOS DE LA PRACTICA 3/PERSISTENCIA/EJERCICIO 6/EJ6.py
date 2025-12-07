import json
from typing import List, Dict, Optional, Set, Tuple

class Libro:
    def __init__(self, codLibro: str, titulo: str, precio: float):
        self.__codLibro = codLibro
        self.__titulo = titulo
        self.__precio = precio

    def mostrar(self):
        print(self.__codLibro, self.__titulo, self.__precio)

    def getCodLibro(self) -> str:
        return self.__codLibro

    def getTitulo(self) -> str:
        return self.__titulo

    def getPrecio(self) -> float:
        return self.__precio


class Prestamo:
    def __init__(self, codCliente: str, codLibro: str, fechaPrestamo: str, cantidad: int):
        self.__codCliente = codCliente
        self.__codLibro = codLibro
        self.__fechaPrestamo = fechaPrestamo
        self.__cantidad = cantidad

    def mostrar(self):
        print(self.__codCliente, self.__codLibro, self.__fechaPrestamo, self.__cantidad)

    def getCodCliente(self) -> str:
        return self.__codCliente

    def getCodLibro(self) -> str:
        return self.__codLibro

    def getCantidad(self) -> int:
        return self.__cantidad


class Cliente:
    def __init__(self, codCliente: str, ci: str, nombre: str, apellido: str):
        self.__codCliente = codCliente
        self.__ci = ci
        self.__nombre = nombre
        self.__apellido = apellido

    def mostrar(self):
        print(self.__codCliente, self.__ci, self.__nombre, self.__apellido)

    def getCodCliente(self) -> str:
        return self.__codCliente

    def getNombreCompleto(self) -> str:
        return f"{self.__nombre} {self.__apellido}"


class ArchLibro:
    def __init__(self, nomArch: str):
        self.__nomArch = nomArch
        self.__l: List[Libro] = []

    def cargar(self):
        with open(self.__nomArch, "r") as f:
            datos = json.load(f)
        self.__l = [Libro(d["codLibro"], d["titulo"], d["precio"]) for d in datos]

    def listar(self):
        for lib in self.__l:
            lib.mostrar()

    def getPorCodigo(self, cod: str) -> Optional[Libro]:
        for lib in self.__l:
            if lib.getCodLibro() == cod:
                return lib
        return None

    def getTodos(self) -> List[Libro]:
        return list(self.__l)

    def librosEntrePrecios(self, x: float, y: float) -> List[Libro]:
        return [lib for lib in self.__l if x <= lib.getPrecio() <= y]

    def librosNuncaVendidos(self, codLibrosVendidos: Set[str]) -> List[Libro]:
        return [lib for lib in self.__l if lib.getCodLibro() not in codLibrosVendidos]


class ArchPrestamo:
    def __init__(self, nomArch: str):
        self.__nomArch = nomArch
        self.__prestamos: List[Prestamo] = []

    def cargar(self):
        with open(self.__nomArch, "r") as f:
            datos = json.load(f)
        self.__prestamos = [
            Prestamo(d["codCliente"], d["codLibro"], d["fechaPrestamo"], d["cantidad"])
            for d in datos
        ]

    def listar(self):
        for p in self.__prestamos:
            p.mostrar()

    def getTodos(self) -> List[Prestamo]:
        return list(self.__prestamos)

    def ingresoTotalPorLibro(self, codLibro: str, archLibros: ArchLibro) -> float:
        libro = archLibros.getPorCodigo(codLibro)
        if not libro:
            return 0.0
        precio = libro.getPrecio()
        return sum(p.getCantidad() * precio for p in self.__prestamos if p.getCodLibro() == codLibro)

    def clientesPorLibro(self, codLibro: str) -> Set[str]:
        return {p.getCodCliente() for p in self.__prestamos if p.getCodLibro() == codLibro}

    def libroMasPrestado(self) -> Optional[Tuple[str, int]]:
        if not self.__prestamos:
            return None
        conteo: Dict[str, int] = {}
        for p in self.__prestamos:
            conteo[p.getCodLibro()] = conteo.get(p.getCodLibro(), 0) + p.getCantidad()
        codMax = max(conteo, key=conteo.get)
        return codMax, conteo[codMax]

    def clienteMasPrestamos(self) -> Optional[Tuple[str, int]]:
        if not self.__prestamos:
            return None
        conteo: Dict[str, int] = {}
        for p in self.__prestamos:
            conteo[p.getCodCliente()] = conteo.get(p.getCodCliente(), 0) + p.getCantidad()
        codMax = max(conteo, key=conteo.get)
        return codMax, conteo[codMax]


class ArchCliente:
    def __init__(self, nomArch: str):
        self.__nomArch = nomArch
        self.__c: List[Cliente] = []

    def cargar(self):
        with open(self.__nomArch, "r") as f:
            datos = json.load(f)
        self.__c = [Cliente(d["codCliente"], d["ci"], d["nombre"], d["apellido"]) for d in datos]

    def listar(self):
        for c in self.__c:
            c.mostrar()

    def getPorCodigo(self, codCliente: str) -> Optional[Cliente]:
        for c in self.__c:
            if c.getCodCliente() == codCliente:
                return c
        return None

    def getTodos(self) -> List[Cliente]:
        return list(self.__c)

    def mostrarClientesPorCodigos(self, codigos: Set[str]):
        for c in self.__c:
            if c.getCodCliente() in codigos:
                c.mostrar()

archLibros = ArchLibro("libros.json")
archPrestamos = ArchPrestamo("prestamos.json")
archClientes = ArchCliente("clientes.json")

archLibros.cargar()
archPrestamos.cargar()
archClientes.cargar()

print("a) Libros entre precios 70 y 100:")
for lib in archLibros.librosEntrePrecios(70, 100):
    lib.mostrar()

cod = "L001"
ingreso = archPrestamos.ingresoTotalPorLibro(cod, archLibros)
print(f"b) Ingreso total por el libro {cod}: {ingreso}")

vendidos = {p.getCodLibro() for p in archPrestamos.getTodos()}
print("c) Libros nunca vendidos:")
for lib in archLibros.librosNuncaVendidos(vendidos):
    lib.mostrar()

codLibro = "L001"
clientes_cod = archPrestamos.clientesPorLibro(codLibro)
print(f"d) Clientes que compraron el libro {codLibro}:")
archClientes.mostrarClientesPorCodigos(clientes_cod)

res_libro = archPrestamos.libroMasPrestado()
if res_libro:
    codMax, cant = res_libro
    libro = archLibros.getPorCodigo(codMax)
    titulo = libro.getTitulo() if libro else codMax
    print(f"e) Libro más prestado: {titulo} ({codMax}) con {cant} unidades")

res_cli = archPrestamos.clienteMasPrestamos()
if res_cli:
    codCli, cant = res_cli
    cli = archClientes.getPorCodigo(codCli)
    nombre = cli.getNombreCompleto() if cli else codCli
    print(f"f) Cliente con más préstamos: {nombre} ({codCli}) con {cant} unidades")
