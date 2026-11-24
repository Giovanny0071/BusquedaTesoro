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
    def __init__(self, nombre, estado,dificultad,tamano,intentos,tablero):
        self.nombre = nombre
        self.estado = estado
        self.dificultad = dificultad
        self.tamano = tamano
        self.intentos = intentos
        self.tablero = tablero


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

