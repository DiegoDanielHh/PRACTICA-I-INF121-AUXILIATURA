class Mp4:
    def __init__(self):
        self.__marca = ""
        self.__capacidadGb = 0.0
        self.__nroCanciones = 0
        self.__canciones = []
        self.__nroVideos = 0
        self.__videos = []
    
    def borrar(self, nombre="", artista="", nombreYPeso=""):
        if nombreYPeso != "":
            partes = nombreYPeso.split()
            nombreBuscar = " ".join(partes[:-1])
            pesoBuscar = partes[-1]
            for i in range(self.__nroCanciones):
                if self.__canciones[i][0] == nombreBuscar and self.__canciones[i][2] == pesoBuscar:
                    self.__canciones.pop(i)
                    self.__nroCanciones -= 1
                    return
        elif nombre != "" and artista != "":
            for i in range(self.__nroCanciones):
                if self.__canciones[i][0] == nombre and self.__canciones[i][1] == artista:
                    self.__canciones.pop(i)
                    self.__nroCanciones -= 1
                    return
        elif nombre != "":
            for i in range(self.__nroCanciones):
                if self.__canciones[i][0] == nombre:
                    self.__canciones.pop(i)
                    self.__nroCanciones -= 1
                    return
    
    def __add__(self, cancion):
        for i in range(self.__nroCanciones):
            if self.__canciones[i][0] == cancion[0] and self.__canciones[i][1] == cancion[1]:
                return 0
        
        peso_cancion = int(cancion[2])
        espacio_usado = 0
        for i in range(self.__nroCanciones):
            espacio_usado += int(self.__canciones[i][2])
        for i in range(self.__nroVideos):
            espacio_usado += int(self.__videos[i][2])
        
        if espacio_usado + peso_cancion <= self.__capacidadGb * 1024:
            self.__canciones.append(cancion)
            self.__nroCanciones += 1
            return 1
        
        return 0
    
    def __sub__(self, video):
        for i in range(self.__nroVideos):
            if self.__videos[i][0] == video[0] and self.__videos[i][1] == video[1]:
                return 0
        
        peso_video = int(video[2])
        espacio_usado = 0
        for i in range(self.__nroCanciones):
            espacio_usado += int(self.__canciones[i][2])
        for i in range(self.__nroVideos):
            espacio_usado += int(self.__videos[i][2])
        
        if espacio_usado + peso_video <= self.__capacidadGb * 1024:
            self.__videos.append(video)
            self.__nroVideos += 1
            return 1
        
        return 0
    
    def mostrar_capacidad(self):
        espacio_usado = 0
        for i in range(self.__nroCanciones):
            espacio_usado += int(self.__canciones[i][2])
        for i in range(self.__nroVideos):
            espacio_usado += int(self.__videos[i][2])
        
        espacio_disponible = self.__capacidadGb * 1024 - espacio_usado
        
        print(f"Capacidad Total: {self.__capacidadGb * 1024} MB")
        print(f"Espacio Usado: {espacio_usado} MB")
        print(f"Espacio Disponible: {espacio_disponible} MB")
        print(f"Canciones: {self.__nroCanciones}")
        print(f"Videos: {self.__nroVideos}")

mp4 = Mp4()
mp4._Mp4__marca = "Sony"
mp4._Mp4__capacidadGb = 8.0

mp4._Mp4__canciones.append(["Back To Black", "Amy Winehouse", "100"])
mp4._Mp4__canciones.append(["Lost On You", "LP", "150"])
mp4._Mp4__nroCanciones = 2

mp4._Mp4__videos.append(["Heathens", "twenty one pilots", "50"])
mp4._Mp4__videos.append(["Harmonica Andromeda", "KSHMR", "70"])
mp4._Mp4__videos.append(["Without Me", "Halsey", "30"])
mp4._Mp4__nroVideos = 3

mp4.mostrar_capacidad()

mp4.borrar(nombre="Back To Black")
mp4.mostrar_capacidad()

mp4 + ["Shape of You", "Ed Sheeran", "120"]
mp4.mostrar_capacidad()

mp4 - ["Blinding Lights", "The Weeknd", "60"]
mp4.mostrar_capacidad()