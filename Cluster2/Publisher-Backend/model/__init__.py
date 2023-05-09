from csv import reader
from datetime import datetime
import os


# Sacar request si no lo vamos a usar
def encolar(ruta, mensaje, channel):
    # ----------------------------------------------------------------------------
    fecha_hora_actual = datetime.now()
    formato = "%H:%M:%S;%d/%m/%Y"
    fecha_hora_formateada = fecha_hora_actual.strftime(formato)


    #Ruta en windows
    archivoW = os.getcwd() + "\\Log\\"+ "logs.txt"
    try:
        file = open(archivoW, 'a+')
    #Ruta en linux
    except:
        archivoL = os.getcwd() + "/files/"+ "logs.txt"
        file = open(archivoL, 'a+')

    file.write(fecha_hora_formateada + "; Encolando token " + mensaje + ";" + ruta + "\n")
    file.close()
    # ----------------------------------------------------------------------------

    channel.basic_publish(exchange='', routing_key=ruta, body = mensaje)