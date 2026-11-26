
def estadisticas_sesion(sesion):
    print("-----Estadisticas-----")



    print("---Partidas totales---")
    print(sesion.getPartidasIniciadas())

    print("---Total partidas finalizadas---")
    print(sesion.getFinalizada())

    print("---Total de partidas ganadas--")
    print(sesion.getganancias())

    print("---Total de partidas abandonadas---")
    print(sesion.getabandonadas())

    print("---Porcentaje de ganadas respecto a finalizadas---")
    print(sesion.getPorcentajeGanadasFInalizadas())

    print("---Numero total de intentos realizados---")
    print(sesion.getNumintentos())

    print("---Media de intentos necesarios para encontrar el tesoro en partidias ganadas---")
    print(sesion.getMediaIntentosNecesariosGanadas())

    print("---Ganadas segun dificultad---")
    ganadas_difi = sesion.getGanadasDificultad()
    print(f"Facil : {ganadas_difi[0]}")
    print(f"Normal : {ganadas_difi[1]}")
    print(f"Dificil: {ganadas_difi[2]}")


    print("---Partidas por usuario---")
    recuento = sesion.partidas_por_usuario(sesion)

    for nombre, cantidad in recuento.items():
        print(f"{nombre}: {cantidad} partidas")


    print("---Grafico de ganadas y perdidas---")
    sesion.graficoGanadas(sesion)

    print("---Grafico por dificultad---")
    sesion.graficoDificultad(sesion)






