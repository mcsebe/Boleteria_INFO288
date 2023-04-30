#!/usr/bin/env python
import pika
from flask import Flask, request, jsonify,json
from common import *
import model

app = Flask(__name__)
app.run(debug=True)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

for i in sysConfig: 
    channel.queue_declare(queue=sysConfig[i])

@app.route('/publisher', methods=['PUT']) 
def getPublisher():
    print(request)
    concierto = request.args.get('concierto')
    if concierto:
        try:
            model.encolar(request, sysConfig[concierto], channel)
            return "Encolado"
        except:
            model.encolar(request, sysConfig["Otros"], channel)
            return "Encolado"
    else:
        print('Parametros incorrectos.')
        return "No encolado"