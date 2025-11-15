class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ArithmeticError("No se puede dividir entre cero")
        return a / b

    def convertir_a_entero(self, cadena):
        return int(cadena)

calc = Calculadora()

print("Suma:", calc.sumar(5, 3))
print("Resta:", calc.restar(10, 4))
print("Multiplicación:", calc.multiplicar(6, 7))
try:
    print("Division:", calc.dividir(10, 0))
except ArithmeticError as e:
    print("Error!!!!!!!!!!:", e)
try:
    numero = calc.convertir_a_entero("123456")
    print("Numero convertido:", numero)

    numero = calc.convertir_a_entero("abcsdfs")
    print("Número convertido:", numero)
except ValueError as e:
    print("Error!!!!!!!!!!!:", e)
