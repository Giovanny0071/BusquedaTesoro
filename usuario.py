
from models import Usuario
from logis import registro as l

def cargar_usuario():
    while True:
        nom = input("Ingrese su nombre: ")
        cont = input("Ingrese su contraseña: ")
        usuario = None

        try:
            with open("usuarios.txt", "r") as f:

                linea = f.readline()

                while linea:

                    datos = linea.strip().split(";")
                    if len(datos) == 3:
                        if datos[0] == nom and datos[1] == cont:
                            usuario = Usuario(datos[0], datos[1],datos[2])

                    linea = f.readline()




            if usuario is None:
                raise FileNotFoundError

            return usuario

        except FileNotFoundError:
            print("Credenciales incorrectas")
            l.registrarLogin("Intento de inicio de sesion fallido","ANONIMO")
            return None

        except PermissionError as e:
            l.registrarLogin("Intento de inicio de sesion fallido","ANONIMO")
            print("No tienes permiso para abrir el fichero")
            print(e)
            return None

        except FileExistsError as e:
            print("El fichero no existe")
            print(e)
            l.registrarLogin("Intento de inicio de sesion fallido","ANONIMO")
            return None

