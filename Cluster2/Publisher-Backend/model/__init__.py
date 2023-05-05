from csv import reader
import requests

# Sacar request si no lo vamos a usar
def encolar(request, ruta, mensaje, channel):
    channel.basic_publish(exchange='', routing_key=ruta, body = mensaje)
