class Buzon:
    def __init__(self, nro, nroC):
        self.__nro = nro
        self.__nroC = nroC
        self.__c = [""] * 50
    
    def getNro(self):
        return self.__nro
    
    def getNroC(self):
        return self.__nroC
    
    def setNroC(self, nroC):
        self.__nroC = nroC
    
    def getCarta(self, i):
        return self.__c[i]
    
    def setCarta(self, i, carta):
        self.__c[i] = carta

class Carta:
    def __init__(self, codigo, descripcion):
        self.__codigo = codigo
        self.__descripcion = descripcion
    
    def getCodigo(self):
        return self.__codigo
    
    def getDescripcion(self):
        return self.__descripcion

buzon1 = Buzon(1, 3)
buzon1.setCarta(0, Carta("C123", "Juan Alvarez para Peter Chaves"))
buzon1.setCarta(1, Carta("C456", "Pepe Mujica para Wilmer Perez"))
buzon1.setCarta(2, Carta("C789", "Paty Vasques para Pepe Mujica"))

buzon2 = Buzon(2, 4)
buzon2.setCarta(0, Carta("C111", "Maria Lopez para Ana Garcia"))
buzon2.setCarta(1, Carta("C222", "Carlos Ruiz para Maria Lopez"))
buzon2.setCarta(2, Carta("C333", "Luis Torres para Carlos Ruiz"))
buzon2.setCarta(3, Carta("C444", "Ana Garcia para Luis Torres"))

buzon3 = Buzon(3, 3)
cartas_buzon3 = [
    Carta("C555", "Pedro Gomez para Sofia Martinez"),
    Carta("C666", "Sofia Martinez para Pedro Gomez"),
    Carta("C777", "Rosa Diaz para Pepe Mujica")
]
for i in range(3):
    buzon3.setCarta(i, cartas_buzon3[i])

buzones = [buzon1, buzon2, buzon3]

carta1 = Carta("C123", "Juan Alvarez para Peter Chaves")
carta2 = Carta("C456", "Pepe Mujica para Wilmer Perez")
carta3 = Carta("C789", "Paty Vasques para Pepe Mujica")

cartas = [carta1, carta2, carta3]

X = "Pepe Mujica"
contador = 0
for carta in cartas:
    if "para " + X in carta.getDescripcion():
        contador += 1

print(f"El destinatario '{X}' recibio {contador} carta(s)")

codigo_eliminar = "C456"
for buzon in buzones:
    for i in range(buzon.getNroC()):
        if buzon.getCarta(i) != "":
            if buzon.getCarta(i).getCodigo() == codigo_eliminar:
                buzon.setCarta(i, "")
                buzon.setNroC(buzon.getNroC() - 1)
                print(f"Carta con codigo '{codigo_eliminar}' eliminada del buzon {buzon.getNro()}")

remitente = "Pepe Mujica"
recibio = False
for carta in cartas:
    if "para " + remitente in carta.getDescripcion():
        recibio = True
        print(f"{remitente} ha recibido alguna carta")

if recibio == False:
    print(f"{remitente} no ha recibido ninguna carta")

palabra = "Pepe"
print(f"\nCartas que contienen la palabra '{palabra}':")
for buzon in buzones:
    for i in range(buzon.getNroC()):
        if buzon.getCarta(i) != "":
            if palabra in buzon.getCarta(i).getDescripcion():
                print(f"Buzon {buzon.getNro()}, Carta {buzon.getCarta(i).getCodigo()}")

print(f"\nCoincidencias con la palabra '{palabra}':")
for buzon in buzones:
    for i in range(buzon.getNroC()):
        if buzon.getCarta(i) != "":
            carta = buzon.getCarta(i)
            if palabra in carta.getDescripcion():
                print(f"Codigo: {carta.getCodigo()}, Remitente y Destinatario: {carta.getDescripcion()}")