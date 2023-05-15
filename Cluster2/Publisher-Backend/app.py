#!/usr/bin/env python
import pika
from flask import Flask, request, jsonify,json
from common import *
import model
import os

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)

# Añadir si se desean colocar más aquinas con rabbit mq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

for i in sysConfig: 
    channel.queue_declare(queue=sysConfig[i])
    

# Ruta que envía el token recibido a la cola correspondiente
@app.route('/publisher', methods=['PUT']) 
def getPublisher():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    data = request.json
    if data["concierto"] and data["mensaje"]:
        try:
            model.encolar(sysConfig[data["concierto"]], data["mensaje"], channel)
            return "Encolado"
        except:
            model.encolar(sysConfig["Otros"], data["mensaje"], channel)
            return "Encolado"
    else:
        print('Parametros incorrectos.')
        return "No encolado"