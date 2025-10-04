class Matriz:
    def __init__(self, valores=None):
        self.matriz = [[0.0]*10 for _ in range(10)]
        if valores is None:
            for i in range(10):
                self.matriz[i][i] = 1.0
        else:
            for i in range(10):
                for j in range(10):
                    self.matriz[i][j] = float(valores[i][j])

    def __add__(self, otra):
        resultado = Matriz([[0.0]*10 for _ in range(10)])
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] + otra.matriz[i][j]
        return resultado

    def __sub__(self, otra):
        resultado = Matriz([[0.0]*10 for _ in range(10)])
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] - otra.matriz[i][j]
        return resultado

    def __eq__(self, otra):
        for i in range(10):
            for j in range(10):
                if self.matriz[i][j] != otra.matriz[i][j]:
                    return False
        return True


m1 = Matriz() 
cero = [[0.0]*10 for _ in range(10)]
m2 = Matriz(cero) 

m3 = m1 + m2
m4 = m1 - m2

print(m1 == m2)   
print(m1 == m3)   
print(m1 == m4)

for i in range(10):
    for j in range(10):
        print(f"{m1.matriz[i][j]:.1f}", end=" ")
    print()


