import logging

class Logis:
    def __init__(self, fichero="registro.log"):
        logging.basicConfig(
            filename=fichero,
            encoding="utf-8",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )


    def registrarLogin(self, mensaje, usuario="-", nivel=logging.INFO):
        logging.log(nivel, "usuario=%s | %s", usuario, mensaje)


registro = Logis()