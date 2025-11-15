class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material
        
class Ropero:
    def __init__(self, material, nroRopas=0):
        self.material = material
        self.ropa = []
        self.nroRopas = nroRopas
        
    def adicionarPrendas(self, N, prendas):
        contador = 0
        for prenda in prendas:
            if contador < N and len(self.ropa) < 20:
                self.ropa.append(prenda)
                self.nroRopas += 1
                contador += 1
            else:
                break
                
    def eliminarPrendas(self, x, y):
        i = 0
        while i < len(self.ropa):
            if self.ropa[i].material == x or self.ropa[i].tipo == y:
                self.ropa.pop(i)
                self.nroRopas -= 1
            else:
                i += 1
                
    def mostrar(self, x, y):
        print("Las prendas son: ")
        for prenda in self.ropa:
            if prenda.material == x and prenda.tipo == y:
                print(f"Tipo: {prenda.tipo}, Material: {prenda.material}")

r1 = Ropa("abrigo", "pelo de oso")
r2 = Ropa("deportivo", "hilo sintetico")
r3 = Ropa("camisa", "algodon")

ropero1 = Ropero("madera")

ropero1.adicionarPrendas(4, [r1, r2, r3])

print(f"Total de prendas: {ropero1.nroRopas}")
ropero1.mostrar("algodon", "camisa")