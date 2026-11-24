class Usuario:



    def __init__(self, nombre, contrasena, rol):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol
        self.partidas = []



    def getNombre(self):
       return self.nombre

    def getContrasena(self):
        return self.contrasena

    def getRol(self):
        return self.rol

    def getPartidas(self):
        return self.partidas


class Partida:
    def __init__(self, nombre,dificultad,tablero,intentosMax,finalizada):
        self.nombre = nombre
        self.estado = "Abandonada"
        self.finalizada = False
        self.dificultad = dificultad
        self.intentos = 0
        self.tablero = tablero
        self.intentosMax = intentosMax


    def getNombre(self):
        return self.nombre

    def getEstado(self):
        return self.estado

    def getDificultad(self):
        return self.dificultad

    def getTamano(self):
        return self.tamano

    def getIntentos(self):
        return self.intentos

    def getTablero(self):
        return self.tablero


    def setEstado(self, estado):
        self.estado = estado

    def setIntentos(self, intentos):
        self.intentos = intentos

