import json
class Jugador:
    def __init__(self, nombre, nivel, puntaje):
        self.nombre = nombre
        self.nivel = nivel
        self.puntaje = puntaje

class ArchivoJugadores:
    def __init__(self):
        self.jugadores = []
    
    def agregar(self, jugador):
        self.jugadores.append(jugador)
    
    def guardar(self):
        with open("jugadores.txt", "w") as f:
            datos = [j.__dict__ for j in self.jugadores]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("jugadores.txt", "r") as f:
                datos = json.load(f)
                self.jugadores = [Jugador(**d) for d in datos]
        except FileNotFoundError:
            self.jugadores = []
    
    def mostrarTodos(self):
        print("todos los jugadores:")
        for j in self.jugadores:
            print(f"{j.nombre} - Nivel: {j.nivel}, Puntaje: {j.puntaje}")
    
    def buscarPorNombre(self, nombre):
        print(f"buscar jugador {nombre}:")
        for j in self.jugadores:
            if j.nombre == nombre:
                print(f"{j.nombre} - Nivel: {j.nivel}, Puntaje: {j.puntaje}")
                return
        print("no encontrado")

class Dataset:
    def __init__(self, nombre, instancias, algoritmo):
        self.nombre = nombre
        self.instancias = instancias
        self.algoritmo = algoritmo

class ArchivoDataset:
    def __init__(self):
        self.datasets = []
    
    def agregar(self, dataset):
        self.datasets.append(dataset)
    
    def guardar(self):
        with open("dataset.txt", "w") as f:
            datos = [d.__dict__ for d in self.datasets]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("dataset.txt", "r") as f:
                datos = json.load(f)
                self.datasets = [Dataset(**d) for d in datos]
        except FileNotFoundError:
            self.datasets = []
    
    def mostrarTodos(self):
        print("todos los datasets:")
        for d in self.datasets:
            print(f"{d.nombre} - Instancias: {d.instancias}, Algoritmo: {d.algoritmo}")
    
    def buscarPorNombre(self, nombre):
        print(f"buscar dataset {nombre}:")
        for d in self.datasets:
            if d.nombre == nombre:
                print(f"{d.nombre} - Instancias: {d.instancias}, Algoritmo: {d.algoritmo}")
                return
        print("no encontrado")

class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

class ArchivoUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def agregar(self, usuario):
        self.usuarios.append(usuario)
    
    def guardar(self):
        with open("usuarios_seguro.txt", "w") as f:
            datos = [u.__dict__ for u in self.usuarios]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("usuarios_seguro.txt", "r") as f:
                datos = json.load(f)
                self.usuarios = [Usuario(**d) for d in datos]
        except FileNotFoundError:
            self.usuarios = []
    
    def mostrarRegistros(self):
        print("registros de usuarios:")
        for u in self.usuarios:
            print(f"Usuario: {u.nombre}, Contraseña: {u.contrasena}")
    
    def buscarPorNombre(self, nombre):
        print(f"buscar usuario {nombre}:")
        for u in self.usuarios:
            if u.nombre == nombre:
                print(f"Usuario: {u.nombre}, Contraseña: {u.contrasena}")
                return
        print("no encontrado")

class Empresa:
    def __init__(self, nombre, rubro, empleados):
        self.nombre = nombre
        self.rubro = rubro
        self.empleados = empleados

class ArchivoEmpresas:
    def __init__(self):
        self.empresas = []
    
    def agregar(self, empresa):
        self.empresas.append(empresa)
    
    def guardar(self):
        with open("empresas.txt", "w") as f:
            datos = [e.__dict__ for e in self.empresas]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("empresas.txt", "r") as f:
                datos = json.load(f)
                self.empresas = [Empresa(**d) for d in datos]
        except FileNotFoundError:
            self.empresas = []
    
    def mostrarTodas(self):
        print("todas las empresas:")
        for e in self.empresas:
            print(f"{e.nombre} - Rubro: {e.rubro}, Empleados: {e.empleados}")
    
    def buscarPorNombre(self, nombre):
        print(f"buscar empresa {nombre}:")
        for e in self.empresas:
            if e.nombre == nombre:
                print(f"{e.nombre} - Rubro: {e.rubro}, Empleados: {e.empleados}")
                return
        print("no encontrado")

class Transaccion:
    def __init__(self, id, monto, fecha):
        self.id = id
        self.monto = monto
        self.fecha = fecha

class ArchivoCobros:
    def __init__(self):
        self.transacciones = []
    
    def agregar(self, transaccion):
        self.transacciones.append(transaccion)
    
    def guardar(self):
        with open("cobros_nfc.txt", "w") as f:
            datos = [t.__dict__ for t in self.transacciones]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("cobros_nfc.txt", "r") as f:
                datos = json.load(f)
                self.transacciones = [Transaccion(**d) for d in datos]
        except FileNotFoundError:
            self.transacciones = []
    
    def mostrarTodas(self):
        print("todas las transacciones:")
        for t in self.transacciones:
            print(f"ID: {t.id}, Monto: {t.monto}, Fecha: {t.fecha}")
    
    def buscarPorId(self, id):
        print(f"buscar transacción ID {id}:")
        for t in self.transacciones:
            if t.id == id:
                print(f"ID: {t.id}, Monto: {t.monto}, Fecha: {t.fecha}")
                return
        print("no encontrado")

class Dispositivo:
    def __init__(self, mac, nombre, velocidad):
        self.mac = mac
        self.nombre = nombre
        self.velocidad = velocidad

class ArchivoDispositivos:
    def __init__(self):
        self.dispositivos = []
    
    def agregar(self, dispositivo):
        self.dispositivos.append(dispositivo)
    
    def guardar(self):
        with open("dispositivos_wifi.txt", "w") as f:
            datos = [d.__dict__ for d in self.dispositivos]
            json.dump(datos, f, indent=2)
    
    def leer(self):
        try:
            with open("dispositivos_wifi.txt", "r") as f:
                datos = json.load(f)
                self.dispositivos = [Dispositivo(**d) for d in datos]
        except FileNotFoundError:
            self.dispositivos = []
    
    def mostrarTodos(self):
        print("todos los dispositivos:")
        for d in self.dispositivos:
            print(f"MAC: {d.mac}, Nombre: {d.nombre}, Velocidad: {d.velocidad}")
    
    def buscarPorMac(self, mac):
        print(f"buscar dispositivo MAC {mac}:")
        for d in self.dispositivos:
            if d.mac == mac:
                print(f"MAC: {d.mac}, Nombre: {d.nombre}, Velocidad: {d.velocidad}")
                return
        print("no encontrado")

print("desarrollo de software")
archJug = ArchivoJugadores()
archJug.agregar(Jugador("Player1", 5, 1500))
archJug.agregar(Jugador("Player2", 3, 800))
archJug.guardar()
archJug.leer()
archJug.mostrarTodos()
archJug.buscarPorNombre("Player1")

print("inteligencia artificial")
archData = ArchivoDataset()
archData.agregar(Dataset("Iris", 150, "KNN"))
archData.agregar(Dataset("Titanic", 891, "Random Forest"))
archData.guardar()
archData.leer()
archData.mostrarTodos()
archData.buscarPorNombre("Iris")

print("seguridad de la información")
archUser = ArchivoUsuarios()
archUser.agregar(Usuario("admin", "admin123"))
archUser.agregar(Usuario("user1", "pass456"))
archUser.guardar()
archUser.leer()
archUser.mostrarRegistros()
archUser.buscarPorNombre("admin")

print("ingeniería en sistemas")
archEmp = ArchivoEmpresas()
archEmp.agregar(Empresa("TechCorp", "Tecnología", 150))
archEmp.agregar(Empresa("BuildCo", "Construcción", 80))
archEmp.guardar()
archEmp.leer()
archEmp.mostrarTodas()
archEmp.buscarPorNombre("TechCorp")

print("ciencias de la computación")
archCobros = ArchivoCobros()
archCobros.agregar(Transaccion(1, 250.50, "2024-12-01"))
archCobros.agregar(Transaccion(2, 180.00, "2024-12-02"))
archCobros.guardar()
archCobros.leer()
archCobros.mostrarTodas()
archCobros.buscarPorId(1)

print("redes y tic")
archDisp = ArchivoDispositivos()
archDisp.agregar(Dispositivo("AA:BB:CC:DD:EE:FF", "Laptop", 300))
archDisp.agregar(Dispositivo("11:22:33:44:55:66", "Smartphone", 150))
archDisp.guardar()
archDisp.leer()
archDisp.mostrarTodos()
archDisp.buscarPorMac("AA:BB:CC:DD:EE:FF")