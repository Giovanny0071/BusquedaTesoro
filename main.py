import logging

from menu import menu
from logis import registro as l


if __name__ == "__main__":
    l.registrarLogin("Inicio de la aplicacion","ANONIMO")

    try:
        menu()
    except Exception as e:
        l.registrarLogin(f"Error de aplicacion: {e}","ANONIMO")
        print(f"Se ha producido un error de aplicacion: {e}")
    finally:
        l.registrarLogin("Fin de la aplicacion","ANONIMO")