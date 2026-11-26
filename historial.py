from helpers.sesion import Sesion
from models import Partida
from partida import mostrar_tablero

def historial_partidas(sesion:Sesion):

    if len(sesion.partidas) != 0:
        for partida in sesion.partidas:
            print("Historial de partidas de la sesion")
            print(f"Usuario: {partida.getNombre()}" )
            print(f"Intentos realizados: {partida.getIntentos()}" )
            print(f"Dificultad: {partida.getDificultad()}" )
            print(f"Estado: {partida.getEstado()}" )
            print(f"Tablero de la partida")
            mostrar_tablero(partida.getTablero())

    else:
        print("No hay partidas en esta sesion")