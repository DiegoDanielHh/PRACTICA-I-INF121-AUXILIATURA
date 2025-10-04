class Fruta:
    def __init__(self, nombre, tipo, nroVitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.nroVitaminas = nroVitaminas
        self.v = [""] * 30
    
    def mostrarVit(self):
        print(f"Vitaminas de {self.nombre}:")
        for i in range(self.nroVitaminas):
            print(self.v[i])

fruta1 = Fruta("kiwi", "subtropical", 3)
fruta1.v[0] = "K"
fruta1.v[1] = "C"
fruta1.v[2] = "E"

fruta2 = Fruta("naranja", "cítrica", 2)
fruta2.v = ["K", "E"] + [""] * 28

fruta3 = Fruta("mango", "tropical", 4)
vitaminas = ["K", "C", "E", "K"]
for i in range(4):
    fruta3.v[i] = vitaminas[i]

frutas = [fruta1, fruta2, fruta3]

fruta_max = frutas[0]
for fruta in frutas:
    if fruta.nroVitaminas > fruta_max.nroVitaminas:
        fruta_max = fruta

print(f"La fruta con más vitaminas es: {fruta_max.nombre}")

fruta1.mostrarVit() 

total = 0
for fruta in frutas:
    if fruta.tipo == "cítrica":
        total += fruta.nroVitaminas

print(f"Total de vitaminas en frutas cítricas: {total}")

for i in range(len(frutas)):
    for j in range(i + 1, len(frutas)):
        if frutas[i].v[0] > frutas[j].v[0]:
            frutas[i], frutas[j] = frutas[j], frutas[i]

print("Frutas ordenadas por vitamina:")
for fruta in frutas:
    print(f"{fruta.nombre}: {fruta.v[0]}")