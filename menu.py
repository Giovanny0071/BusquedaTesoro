
def menu():

   while True:
    print("Bienvenido a la busqueda del tesoro")
    print("1 - Iniciar sesion")
    print("2 - Registrarse")
    print("3 - Salir")
    opt = int(input("Selecciona una opcion: "))

    if opt == 1:

       pass #cargar_usuario()

       if usuario is not None:
           #lo llevo al menu de juego como tal depende si es admin o no y log
            pass
    elif opt == 2:
        pass
        #Lo registro y log

    elif opt == 3:
        print("----FIN DEL PROGRAMA----")
        #log
        break


    else:
        print("Opcion invalida")
        #log


def menu_juego_usuario():
    while True:
        print("1. Iniciar nueva partida")
        print("2. Cerrar sesion")
        print("3. Salir")
        try:
            opt = input("Selecciona una opcion: ")

            if opt == "1":
                #nueva_partida()
                pass

            elif opt == "2":
                return

            elif opt == "3":
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
            #nueva_partida()
            pass

        elif opt == "2":
            #estadisticas_sesion()
            pass

        elif opt == "3":
            #historial_partidas()
            pass

        elif opt == "4":
            return

        elif opt == "5":
            print("----FIN DEL PROGRAMA----")
            break

        else:
            print("Opcion invalida")
















