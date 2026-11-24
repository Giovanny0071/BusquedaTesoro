from helpers import sesion
from helpers.sesion import Sesion
from models import Partida, Usuario
import random
from logis import Logis as l
def nueva_partida(sesion:Sesion):


   while(True):
        dificultad = input("Que dificultad quieres?   (1) Facil | (2) Normal | (3) Dificil ")

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
        else:
            print("Dificultad invalida")

        try:
             intentosMax = int(input("Cuantos intentos maximos quieres?"))
             break
        except ValueError:
            print("No has puesto unos intentos maximos validos")
           continue


   l.registrarlog(f"Partida iniciada | dificultad={dificultad}",sesion.usuarioLog.getNombre())

   partida = Partida(sesion.usuarioLog.getNombre(),dificultad,tablero,intentosMax)
   jugar_partida(sesion,partida)

def jugar_partida(sesion:Sesion,partida:Partida):
    numPosTesA = random.randint(0,len(partida.tablero))
    numPosTesB = random.randint(0,len(partida.tablero))
    intentos = 0
    ganada = False
    posicion_tesoro = [numPosTesA,numPosTesB]
    tableroRevelo = partida.tablero
    partida.tablero[posicion_tesoro[0],posicion_tesoro[1]] = "💎"
    pistas = False
    while(partida.intentosMax != intentos):
        mostrar_tablero(tableroRevelo)
        if(intentos > 3):
            pistas = True
        try:
            fila = int(input("Dime que fila quieres mirar"))
            columna = int(input("Dime que columna quieres mirar"))
            abandonar = input("Quieres abandonar la partida? (pon 's' para abandonar)")
            if(abandonar.lower() == "s"):
                break

            if (partida.tablero[fila, columna] == "0"):
                print("No puedes mirar de nuevo la misma casilla")
            else:
                l.registrarlog(f"Coordenadas seleccionadas | fila={fila} | columna={columna}",sesion.usuarioLog.getNombre())
                if (pistas):
                  quierePista = input("Quieres una pista? (s/n)")
                  if(quierePista == "s"):
                      l.registrarlog(f"Pista solicitada | fila={fila} | columna={columna}", sesion.usuarioLog.getNombre())
                      print(cargar_pista(fila,columna,posicion_tesoro,sesion))
                  elif(quierePista == "n"):
                      print("Has decidido que no quieres pista")
                  else:
                      raise ValueError
                if(partida.tablero[fila,columna] != "💎"):
                        intentos += 1
                        tableroRevelo[fila, columna] = "0"
                else:
                    ganada = True
                    break
        except ValueError:
            print("Respuesta no valida")
            continue
        except Exception:
            print("Te has ido del tablero")
            continue

    partida.finalizada = True
    if(ganada):
        partida.intentos = intentos
        partida.estado = "Ganada"
        print("Felicidades has ganado")
    elif(abandonar):
        partida.intentos = partida.intentos
        partida.estado = "Abandonada"
        print("Has Abandonado")
    else:
        partida.intentos = intentos
        partida.estado = "Perdida"
        print("Has Perdido")

    l.registrarlog(f"Partida finalizada | resultado={partida.estado} | intentos={partida.intentos}",sesion.usuarioLog.getNombre())
    sesion.partidas.append(partida)






def mostrar_tablero(tablero):
    for i in tablero:
        print()
        for j in i:
            print(j, end=" ")


def cargar_pista(fila, columna, posicion_tesoro,sesion:Sesion):
    fila_tesoro = posicion_tesoro[0]
    columna_tesoro = posicion_tesoro[1]

    diferencia_fila = abs(fila - fila_tesoro)
    diferencia_columna = abs(columna - columna_tesoro)

    if max(diferencia_fila, diferencia_columna) == 1:
        resultado =  "Estás cerca del tesoro"


    else:
     resultado = "Estás lejos del tesoro"

    l.registrarlog(f"Resultado de la pista | {resultado}", sesion.usuarioLog.getNombre())
    return resultado