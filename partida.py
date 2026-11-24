from helpers.sesion import Sesion
from models import Partida, Usuario
import random

def nueva_partida(sesion:Sesion):


   while(True):
        dificultad = input("Que dificultad quieres?   (1) Facil | (2) Normal | (3) Dificil ")
        try:
             intentosMax = int(input("Cuantos intentos maximos quieres?"))
        except ValueError:
            print("No has puesto unos intentos maximos validos")

        if dificultad == "1":
            tablero  = [
                ["*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*"],
            ]
            break
        elif dificultad == "2":
            tablero = [
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*"],
            ]
            break
        elif dificultad == "3":
            tablero = [
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ]
            break
        else:
            print("Dificultad invalida")

   partida = Partida(sesion.usuarioLog.getNombre(),dificultad,tablero,intentosMax)
   sesion.partidas.append(partida)
   jugar_partida(sesion,partida)

def jugar_partida(sesion:Sesion,partida:Partida):
    numPosTesA = random.randint(0,len(partida.tablero))
    numPosTesB = random.randint(0,len(partida.tablero))
    intentos = 0
    posicion_tesoro = [numPosTesA,numPosTesB]
    tableroRevelo = partida.tablero
    partida.tablero[posicion_tesoro[0],posicion_tesoro[1]] = "💎"
    pistas = False
    while(partida.intentosMax != intentos):
        mostrar_tablero(partida.tablero)
        if(intentos >= 3):
            pistas = True
        try:
            fila = int(input("Dime que fila quieres mirar"))
            columna = int(input("Dime que columna quieres mirar"))
            if (pistas):
              quierePista = input("Quieres una pista? (s/n)")
              if(quierePista == "s"):
                  #cargar_pista
                  pass
              elif(quierePista == "n"):
                  print("Has decidido que no quieres pista")

              else:
                  raise ValueError

            if(partida.tablero[fila,columna] != "💎"):
                intentos += 1
                tableroRevelo[fila,columna] = "0"

        except ValueError:
            print("Respuesta no valida")
        except Exception:
            print("Te has ido del tablero")







def mostrar_tablero(tablero):
    for i in tablero:
        print()
        for j in i:
            print(j, end=" ")
