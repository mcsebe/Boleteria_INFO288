from csv import reader
from datetime import datetime
import os


# Función que envía el token a la cola correspondiente
def queueUp(route, message, channel, file, format):
    # Escribe en el log de eventos
    # ----------------------------------------------------------------------------
    current_time = datetime.now()
    current_time_formated = current_time.strftime(format)
    file.write(current_time_formated + "; Encolando token " +
               message + ";" + route + "\n")

    channel.basic_publish(exchange='', routing_key=route, body=message)
