class Usuario:



    def __init__(self, nombre, contrasena, rol,partidas):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol
        self.partidas = partidas



    def getNombre(self):
       return self.nombre

    def getContrasena(self):
        return self.contrasena

    def getRol(self):
        return self.rol

    def getPartidas(self):
        return self.partidas

    