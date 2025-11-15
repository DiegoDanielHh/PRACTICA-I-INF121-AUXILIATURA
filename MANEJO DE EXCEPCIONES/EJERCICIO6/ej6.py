class FondosInsuficientesException(Exception):
    pass

class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise FondosInsuficientesException(
                f"Fondos insuficientes"
            )
        self.saldo -= monto

    def mostrarInfo(self):
        print(f"Cuenta: {self.numeroCuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

cuenta = CuentaBancaria("12345", "Juan Perez", 1000)
cuenta.mostrarInfo()

try:
    cuenta.depositar(500)
    print("\nDepósito válido realizado.")
    cuenta.mostrarInfo()
except ValueError as e:
    print("Error en depósito:", e)

try:
    cuenta.depositar(-200)
except ValueError as e:
    print("\nError en depósito:", e)

try:
    cuenta.retirar(300)
    print("\nRetiro válido realizado.")
    cuenta.mostrarInfo()
except FondosInsuficientesException as e:
    print("Error en retiro:", e)

try:
    cuenta.retirar(2000)
except FondosInsuficientesException as e:
    print("\nError en retiro:", e)
