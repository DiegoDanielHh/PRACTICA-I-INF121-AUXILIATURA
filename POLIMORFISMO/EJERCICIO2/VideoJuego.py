from multimethod import multimethod
class Videojuego:
    @multimethod
    def __init__(self, nombre: str, plataforma: str, cantidad: int):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad = cantidad

    @multimethod
    def __init__(self, nombre: str, plataforma: str):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad = 0

    @multimethod
    def agregarJugadores(self):
        self.cantidad += 1
        return self.cantidad

    @multimethod
    def agregarJugadores(self, cantidad: int):
        self.cantidad += cantidad
        return self.cantidad

    def mostrar(self):
        return print(f"Nombre: {self.nombre}\nPlataforma: {self.plataforma}\nCantidad: {self.cantidad}")

v1 = Videojuego("FIFA", "PlayStation", 2)
v2 = Videojuego("Minecraft", "PC")

print("Videojuego 1:")
v1.mostrar()
v1.agregarJugadores()
print("\nDespués de agregar 1 jugador:")
v1.mostrar()

print("\nVideojuego 2:")
v2.mostrar()
num = int(input("\nIngrese la cantidad de jugadores a agregar: "))
v2.agregarJugadores(num)
print("\nDespués de agregar jugadores:")
v2.mostrar()
