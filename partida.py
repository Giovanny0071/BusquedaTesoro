from helpers.sesion import Sesion
from models import Partida, Usuario
import random

def nueva_partida(sesion:Sesion):


   while(True):
        dificultad = input("Que dificultad quieres?   (1) Facil | (2) Normal | (3) Dificil ")

        if dificultad == "1":
            tablero  = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
            break
        elif dificultad == "2":
            tablero = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
            break
        elif dificultad == "3":
            tablero = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
            break
        else:
            print("Dificultad invalida")

   partida = Partida(sesion.usuarioLog.getNombre(),dificultad,tablero)
   sesion.partidas.append(partida)
   jugar_partida(sesion,partida)

def jugar_partida(sesion:Sesion,partida:Partida):
    numPosTesA = random.randint(0,len(partida.tablero))
    numPosTesB = random.randint(0,len(partida.tablero))

    posicion_tesoro = [numPosTesA,numPosTesB]

    partida.tablero[posicion_tesoro[0],posicion_tesoro[1]] = "💎"
    