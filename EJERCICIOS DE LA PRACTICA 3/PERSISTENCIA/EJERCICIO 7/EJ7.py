import json

class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.ci = ci

class Nino(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci, edad, peso, talla):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, ci)
        self.edad = edad
        self.peso = peso
        self.talla = talla

class ArchNino:
    def __init__(self):
        self.ninos = []
    
    def crear(self, nino):
        self.ninos.append(nino)
    
    def guardar(self):
        with open('ninos.json', 'w') as f:
            datos = [n.__dict__ for n in self.ninos]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open('ninos.json', 'r') as f:
                datos = json.load(f)
                self.ninos = [Nino(**d) for d in datos]
        except FileNotFoundError:
            self.ninos = []
    
    def listar(self):
        for n in self.ninos:
            print(f"{n.nombre} {n.apellidoPaterno} - Edad: {n.edad}, Peso: {n.peso}, Talla: {n.talla}")
    
    def mostrar(self):
        self.listar()
    
    def peso_adecuado(self):
        count = 0
        for n in self.ninos:
            if 3 <= n.edad <= 5 and 14 <= n.peso <= 18 and 95 <= n.talla <= 110:
                count += 1
            elif 6 <= n.edad <= 8 and 19 <= n.peso <= 25 and 111 <= n.talla <= 130:
                count += 1
            elif 9 <= n.edad <= 12 and 26 <= n.peso <= 40 and 131 <= n.talla <= 150:
                count += 1
        print(f"Niños con peso y talla adecuados: {count}")
    
    def peso_inadecuado(self):
        print("Niños con peso o talla inadecuados:")
        for n in self.ninos:
            adecuado = False
            if 3 <= n.edad <= 5 and 14 <= n.peso <= 18 and 95 <= n.talla <= 110:
                adecuado = True
            elif 6 <= n.edad <= 8 and 19 <= n.peso <= 25 and 111 <= n.talla <= 130:
                adecuado = True
            elif 9 <= n.edad <= 12 and 26 <= n.peso <= 40 and 131 <= n.talla <= 150:
                adecuado = True
            
            if not adecuado:
                print(f"{n.nombre} {n.apellidoPaterno} - Edad: {n.edad}, Peso: {n.peso}, Talla: {n.talla}")
    
    def promedio_edad(self):
        if self.ninos:
            promedio = sum(n.edad for n in self.ninos) / len(self.ninos)
            print(f"Promedio de edad: {promedio:.2f}")
    
    def buscar_ci(self, ci):
        for n in self.ninos:
            if n.ci == ci:
                print(f"Encontrado: {n.nombre} {n.apellidoPaterno} - Edad: {n.edad}, Peso: {n.peso}, Talla: {n.talla}")
                return
        print("No encontrado")
    
    def talla_alta(self):
        if self.ninos:
            max_talla = max(n.talla for n in self.ninos)
            print(f"Niños con talla más alta ({max_talla}):")
            for n in self.ninos:
                if n.talla == max_talla:
                    print(f"{n.nombre} {n.apellidoPaterno}")

arch = ArchNino()

arch.crear(Nino("Juan", "Perez", "Lopez", 12345, 5, 16, 105))
arch.crear(Nino("Maria", "Gomez", "Ruiz", 23456, 7, 22, 120))
arch.crear(Nino("Pedro", "Torres", "Diaz", 34567, 10, 35, 140))
arch.crear(Nino("Ana", "Silva", "Mendez", 45678, 4, 12, 90))
arch.crear(Nino("Luis", "Castro", "Vega", 56789, 8, 28, 135))

arch.guardar()

arch.leer()

print("LISTADO DE NIÑOS")
arch.listar()

print("\nPESO Y TALLA ADECUADOS")
arch.peso_adecuado()

print("\nPESO O TALLA INADECUADOS")
arch.peso_inadecuado()

print("\nPROMEDIO DE EDAD")
arch.promedio_edad()

print("\nBUSCAR POR CI")
arch.buscar_ci(23456)

print("\nTALLA MÁS ALTA")
arch.talla_alta()