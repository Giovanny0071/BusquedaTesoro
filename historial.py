from helpers.sesion import Sesion
from models import Partida
from partida import mostrar_tablero

def historial_partidas(sesion:Sesion):
    for partida in sesion.partidas:
        print("Historial de partidas de la sesion")
        print(f"Usuario: {partida.getNombre()}" )
        print(f"Tablero de la partida")
        mostrar_tablero(partida.getTablero())
        print(f"Intentos realizados: f{partida.getIntentos()}" )
        print(f"Dificultad: {partida.getDificultad()}" )
        print(f"Estado: {partida.getEstado()}" )

