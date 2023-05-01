#!/usr/bin/env python
import pika
from flask import Flask, request, jsonify,json
from common import *
import model

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)

# Añadir si se desean colocar más aquinas con rabbit mq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

for i in sysConfig: 
    channel.queue_declare(queue=sysConfig[i])
    

@app.route('/publisher', methods=['PUT']) 
def getPublisher():
    data = request.json
    if data["concierto"] and data["mensaje"]:
        try:
            # Sacar request si no lo vamos a usar
            model.encolar(request, sysConfig[data["concierto"]], data["mensaje"], channel)
            return "Encolado"
        except:
            # Sacar request si no lo vamos a usar
            model.encolar(request, sysConfig["Otros"], data["mensaje"], channel)
            return "Encolado"
    else:
        print('Parametros incorrectos.')
        return "No encolado"