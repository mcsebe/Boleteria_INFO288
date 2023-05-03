from flask import Flask, request, jsonify,json
from common import app, sysConfig
from controller import *
import model
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare("desencolar")

@app.route('/capacidad', methods=['GET']) 
def getCapacidad():
    if(request.args.get("id_concierto")):
        concierto = int(request.args.get("id_concierto"))
    else:
        concierto = int(request.json["id_concierto"])
    total = model.capacidad(sysConfig["dbConnConfig"], concierto)
    return total

@app.route('/disponible', methods=['GET']) 
def getDisponibles():
    if(request.args.get("id_concierto")):
        concierto = int(request.args.get("id_concierto"))
    else:
        concierto = int(request.json["id_concierto"])
    total = set(range(1, model.capacidad(sysConfig["dbConnConfig"], concierto)[0] + 1))
    ocupados = set(model.disponible(sysConfig["dbConnConfig"], concierto))
    return list(total - ocupados)


@app.route('/subir', methods=['POST']) 
def createReserva():
    data = request.json
    return model.insert(sysConfig["dbConnConfig"],data)
