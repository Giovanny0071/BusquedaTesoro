
from models import Usuario
class Sesion:
    def __init__(self):
        self.usuarioLog = Usuario | None
        self.partidas = []


    def getUsuarioLog(self):
        return self.usuarioLog




    def setUsuarioLog(self,usuarioLog):
        self.usuarioLog = usuarioLog


    def getPartidas(self):
        return self.partidas


    def setPartida(self,partida):
        self.partidas = self.partidas.append(self,partida)


    def getPartidasFinalizadas(self):
        cont = 0
        for partida in self.partidas:
            if partida.estado == "Ganada" or partida.estado == "Perdida":
                cont += 1

        if cont == 0:
            print("No hay Partidas Finalizadas")

        return cont

    def getPartidasAbandonadas(self):
        cont = 0
        for partida in self.partidas:
            if partida.estado == "Abandonada":
                cont += 1

        if cont == 0:
            print("No hay Partidas abandonadas")

        return cont

    def getPartidasGanadas(self):
        ganadas = 0
        for partida in self.partidas:
            if partida.estado == "Ganadas":
                ganadas += 1

        if ganadas == 0:
            print("No hay Partidas ganadas")

        return ganadas

    def getPorcentajeGanadasFInalizadas(self):

        if self.getPartidasFinalizadas() == 0:
            return 0

        return self.getPartidasGanadas() / self.getPartidasFinalizadas() * 100




    def getMediaIntentos(self):
        intentos = 0
        for partida in self.partidas:
            if(partida.estado == "Ganada"):
                 intentos += partida.intentos
        if (self.getPartidasGanadas() == 0):
            return 0

        return intentos / self.getPartidasGanadas()



    def getGanadasDificultad(self):
        facil = 0
        Normal = 0
        Dificil = 0
        GanadasDificultad = []
        for partida in self.partidas:
            if partida.estado == "Ganada":

                if partida.dificultad == "Facil":
                    facil += 1
                elif partida.dificultad == "Normal":
                    Normal += 1
                elif  partida.dificultad == "Dificil":
                    Dificil += 1

                GanadasDificultad[0] = facil
                GanadasDificultad[1] = Normal
                GanadasDificultad[2] = Dificil

        return GanadasDificultad
