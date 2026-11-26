from menu import menu
from logis import registro as l



if __name__ == '__main__':
    try:
        menu()
    except BaseException as e:
        l.registrarLogin(
            "ERROR",
            f"Se ha producido un error de aplicacion {e}"
        )
        print(f"Se ha producido un error de aplicacion {e}")