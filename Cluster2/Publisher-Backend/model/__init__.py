from csv import reader
from datetime import datetime
import os


# Función que envía el token a la cola correspondiente
def queueUp(route, message, channel):
    # Escribe en el log de eventos
    # ----------------------------------------------------------------------------
    current_time = datetime.now()
    format = "%H:%M:%S;%d/%m/%Y"
    current_time_formated = current_time.strftime(format)

    # Ruta en windows
    logW = os.getcwd() + "\\Log\\" + "logs.txt"
    try:
        file = open(logW, 'a+')
    # Ruta en linux
    except:
        logL = os.getcwd() + "/files/" + "logs.txt"
        file = open(logL, 'a+')

    file.write(current_time_formated + "; Encolando token " +
               message + ";" + route + "\n")
    file.close()
    # ----------------------------------------------------------------------------

    channel.basic_publish(exchange='', routing_key=route, body=message)
