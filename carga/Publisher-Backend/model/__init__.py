from csv import reader
import requests

def encolar(request, ruta, channel):
    channel.basic_publish(exchange='', routing_key=ruta, body = "equisde")
