from csv import reader
from datetime import datetime
import os


# Función que envía el token a la cola correspondiente
def queueUp(route, message, channel, logger):
    # Escribe en el log de eventos
    # ----------------------------------------------------------------------------
    logger.info("Encolando token " +  message + ";" + route)
    channel.basic_publish(exchange='', routing_key=route, body=message)
