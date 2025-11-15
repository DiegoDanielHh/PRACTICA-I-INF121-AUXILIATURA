class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci


class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad


class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket


class Charla:
    def __init__(self, lugar, nombreCharla, speaker, nc):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.S = speaker      
        self.nc = nc
        self.P = []         

    def agregar_participante(self, participante):
        if len(self.P) < 50:
            self.P.append(participante)


class Evento:
    def __init__(self, nombre, nc):
        self.nombre = nombre
        self.nc = nc
        self.C = [] 

    def agregar_charla(self, charla):
        if len(self.C) < 50:
            self.C.append(charla)

    def edad_promedio_participantes(self):
        total = 0
        cantidad = 0
        for charla in self.C:
            for p in charla.P:
                total += p.edad
                cantidad += 1
        if cantidad == 0:
            return 0
        return total / cantidad

    def persona_en_evento(self, X, Y):
        for charla in self.C:
            # revisar speaker
            if (charla.S.nombre == X and charla.S.apellido == Y):
                return True
            # revisar participantes
            for p in charla.P:
                if p.nombre == X and p.apellido == Y:
                    return True
        return False

    def eliminar_charlas_speaker(self, X):
        nuevas_charlas = []
        for charla in self.C:
            if charla.S.ci != X:
                nuevas_charlas.append(charla)
        self.C = nuevas_charlas

    def ordenar_charlas_por_participantes(self):
        for i in range(len(self.C) - 1):
            for j in range(i + 1, len(self.C)):
                if len(self.C[i].P) < len(self.C[j].P):
                    temp = self.C[i]
                    self.C[i] = self.C[j]
                    self.C[j] = temp

s1 = Speaker("Ana", "Lopez", 25, 1239828, "IA")
s2 = Speaker("Alan", "Brito", 40, 93848943, "Ciberseguridad")

part1 = Participante("Luis", "Perez", 30, 12345678, 101)
part2 = Participante("Maria", "Gomez", 28, 87654321, 102)

charla1 = Charla("Auditorio A", "Python Básico", s1, 1)
charla1.agregar_participante(part1)
charla1.agregar_participante(part2)

charla2 = Charla("Sala B", "Hacking Ético", s2, 2)
charla2.agregar_participante(part1)

charla3 = Charla("Sala C", "Bases de Datos", s1, 3)
charla3.agregar_participante(part2)

evento = Evento("SKYNET SERÁ REAL", 3)
evento.agregar_charla(charla3)
evento.agregar_charla(charla1)
evento.agregar_charla(charla2)

print(f"Edad promedio de participantes: {evento.edad_promedio_participantes()}")
print(f"Está Luis Perez en el evento?: {evento.persona_en_evento("Luis", "Perez")}")

print("\nCharlas antes de eliminar:")
for c in evento.C:
    print(f"{c.nombreCharla}")

evento.eliminar_charlas_speaker(93848943)

print("Charlas después de eliminar:")
for c in evento.C:
    print(f"{c.nombreCharla}")

print("\nCharlas antes de ordenar:")
for c in evento.C:
    print(f"{c.nombreCharla} con {len(c.P)} participantes")

evento.ordenar_charlas_por_participantes()

print("Charlas después de ordenar:")
for c in evento.C:
    print(f"{c.nombreCharla} con {len(c.P)} participantes")
