from helpers.sesion import Sesion
from models import Usuario
from logis import Logis as l
from usuario import Usuario as u
sesion = Sesion()

def menu():

   while True:
    print("Bienvenido a la busqueda del tesoro")
    print("1 - Iniciar sesion")
    print("2 - Salir")
    opt = int(input("Selecciona una opcion: "))

    if opt == 1:

       sesion.usuarioLog = u.cargar_usuario()

       if sesion.usuarioLog is not None:
           l.registrarLogin("Inicio de sesion",sesion.usuarioLog.getNombre())
           if sesion.usuarioLog.getRol() == "Usuario":
               menu_juego_usuario()
           else:
               menu_juego_admin()

    elif opt == 2:
        l.registrarLogin("Cierre del programa","ANONIMO")
        print("----FIN DEL PROGRAMA----")

        break
    else:
        print("Opcion invalida")



def menu_juego_usuario():
    global sesion
    while True:
        print("1. Iniciar nueva partida")
        print("2. Cerrar sesion")
        print("3. Salir")
        try:
            opt = input("Selecciona una opcion: ")

            if opt == "1":
                #nueva_partida()
                l.registrarLogin(sesion.usuarioLog,"Partida Nueva",sesion.usuarioLog.getNombre() )
                pass

            elif opt == "2":
                l.registrarLogin(sesion.usuarioLog,"Cerrar sesion",sesion.usuarioLog.getNombre())
                sesion.usuarioLog = None
                return

            elif opt == "3":
                l.registrarLogin(sesion.usuarioLog,"Fin del programa",sesion.usuarioLog.getNombre())
                print("----FIN DEL PROGRAMA----")
                break
            else:
                print("Opcion invalida")
        except Exception as e:
            print("Ha ocurrido una excepcion")
            print(e)



def menu_juego_admin():

    while True:
        print("1. Iniciar nueva partida")
        print("2. Consultar las estadisticas de la sesion")
        print("3. Consultar el historial de partidas de la sesion")
        print("4. Cerrar Sesion")
        print("5. Salir")

        opt = input("Selecciona una opcion: ")

        if opt == "1":
            l.registrarLogin("Partida Nueva", sesion.usuarioLog.getNombre())
            #nueva_partida()
            pass

        elif opt == "2":
            l.registrarLogin("Consultar estadisticas", sesion.usuarioLog.getNombre())
            #estadisticas_sesion()
            pass

        elif opt == "3":
            l.registrarLogin("Consultar historial", sesion.usuarioLog.getNombre())
            #historial_partidas()
            pass

        elif opt == "4":
            l.registrarLogin("Cerrar sesion", sesion.usuarioLog.getNombre())
            sesion.usuarioLog = None
            return

        elif opt == "5":
            l.registrarLogin("Salir del programa", sesion.usuarioLog.getNombre())
            print("----FIN DEL PROGRAMA----")
            break

        else:
            print("Opcion invalida")
















