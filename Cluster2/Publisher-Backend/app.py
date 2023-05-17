#!/usr/bin/env python
import pika
from flask import Flask, request, jsonify, json
from common import *
import model
import os

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)

# Iniciando la conexión con RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

for i in sysConfig:
    channel.queue_declare(queue=sysConfig[i])

# Abriendo el archivo Log
format = "%H:%M:%S;%d/%m/%Y"
logW = os.getcwd() + "\\Log\\" + "logs.txt"
try:
    file = open(logW, 'a+')
except:
    logL = os.getcwd() + "/files/" + "logs.txt"
    file = open(logL, 'a+')

# Ruta que envía el token recibido a la cola correspondiente
@app.route('/publisher', methods=['PUT'])
def getPublisher():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    data = request.json
    if data["concierto"] and data["mensaje"]:
        try:
            model.queueUp(sysConfig[data["concierto"]],data["mensaje"], channel, file, format)
            return "Encolado"
        except:
            model.queueUp(sysConfig["Otros"], data["mensaje"], channel, file, format)
            return "Encolado"
    else:
        print('Parametros incorrectos.')
        return "No encolado"
