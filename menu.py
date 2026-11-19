

def menu():

   while True:
    print("Bienvenido a la busqueda del tesoro")
    print("1 - Iniciar sesion")
    print("2 - Registrarse")
    print("3 - Salir")
    opt = int(input("Selecciona una opcion: "))

    if opt == 1:
       cliente = None #cargar_usuario()

       if cliente is not None:
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







