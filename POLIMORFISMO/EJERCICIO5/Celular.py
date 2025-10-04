class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp


    def __pos__(self):
        return Celular(self.nroTel, self.dueño, self.espacio, self.ram, self.nroApp + 10)

    def __neg__(self):
        return Celular(self.nroTel, self.dueño, self.espacio - 5, self.ram, self.nroApp)

    def __str__(self):
        return f"nroTel={self.nroTel}, dueño={self.dueño}, espacio={self.espacio}GB, ram={self.ram}GB, nroApp={self.nroApp}"

cel = Celular(24, "Juan", 128, 8, 15)

print("Antes de operadores:")
print(cel)

cel = +cel
print("\nDespués de ++ :")
print(cel)

cel = -cel
print("\nDespués de -- :")
print(cel)
