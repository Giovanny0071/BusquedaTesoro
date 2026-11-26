import matplotlib.pyplot as plt
from models import Usuario, Partida


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
        self.partidas.append(partida)



    def getPartidasIniciadas(self):
        return len(self.getPartidas())

    def getPartidasFinalizadas(self):
        cont = 0
        for partida in self.partidas:
            if partida.getfinalizada() == True:
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
            if partida.estado == "Ganada":
                ganadas += 1

        if ganadas == 0:
            print("No hay Partidas ganadas")

        return ganadas

    def getPorcentajeGanadasFInalizadas(self):

        if self.getPartidasFinalizadas() == 0:
            return 0

        return self.getPartidasGanadas() / self.getPartidasFinalizadas() * 100


    def getPerdidas(self):
        perdidas = 0
        for partida in self.partidas:
            if partida.estado == "Perdida":
                perdidas += 1

        if perdidas == 0:
            print("No hay Partidas perdidas")

        return perdidas

    def getMediaIntentos(self):
        intentos = 0
        for partida in self.partidas:
            if(partida.estado == "Ganada"):
                 intentos += partida.intentos
        if (self.getPartidasGanadas() == 0):
            return 0

        return intentos / self.getPartidasGanadas()

    def getGanadasDificultad(self):
        ganadas_difi = [0, 0, 0]

        for partida in self.getPartidas():
            if partida.estado == "Ganada":
                if partida.dificultad == "1":
                    ganadas_difi[0] += 1
                elif partida.dificultad == "2":
                    ganadas_difi[1] += 1
                elif partida.dificultad == "3":
                    ganadas_difi[2] += 1

        return ganadas_difi


    def getTodosIntentos(self):
        intentos = 0
        for partida in self.getPartidas():
            intentos += partida.intentos

        return intentos


    def partidas_por_usuario(self):
        recuento = {}

        for partida in self.partidas:
            nombre = partida.getNombre()  # Atributo donde guardas el nombre del jugador

            if nombre in recuento:
                recuento[nombre] += 1
            else:
                recuento[nombre] = 1

        return recuento

    def getPartidasPorDificultad(self):
        totales = [0, 0, 0]

        for partida in self.getPartidas():
            if partida.dificultad == "1":
                totales[0] += 1
            elif partida.dificultad == "2":
                totales[1] += 1
            elif partida.dificultad == "3":
                totales[2] += 1

        return totales


    def grafico_ganadas_perdidas(self):
        ganadas = self.getPartidasGanadas()
        perdidas = self.getPerdidas()

        plt.figure()
        plt.bar(["Ganadas", "Perdidas"], [ganadas, perdidas])
        plt.title("Partidas ganadas y perdidas")
        plt.ylabel("Número de partidas")
        plt.show()

    def grafico_dificultad(self):
        partidas_difi = self.getPartidasPorDificultad()

        plt.figure()
        plt.bar(["Fácil", "Normal", "Difícil"], partidas_difi)
        plt.title("Partidas por dificultad")
        plt.ylabel("Número de partidas")
        plt.show()