#!/usr/bin/env python
import pika
from flask import Flask, request, jsonify, json
from common import *
import model
import os
import time
import logging
import re

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)
time.sleep(30)
# Iniciando la conexión con RabbitMQ
credentials = pika.PlainCredentials(sysConfig["rabbit"]["user"],sysConfig["rabbit"]["password"])
connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq",5672,'/',credentials))
channel = connection.channel()


for i in sysConfig:
    if(type(sysConfig[i]) == str and i !="log_rute"):
        channel.queue_declare(queue=sysConfig[i])


app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
logging.getLogger("pika").propagate = False

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(sysConfig["log_rute"])
handler.setFormatter(logging.Formatter('%(asctime)s;%(message)s', datefmt="%H:%M:%S;%d/%m/%Y"))
logger.addHandler(handler)

#Limpia los strings de "" ; \
def clean(unverified_input):
    return(re.sub(r'[\'";]', '', unverified_input))

# Ruta que envía el token recibido a la cola correspondiente
@app.route('/publisher', methods=['PUT'])
def getPublisher():
    credentials = pika.PlainCredentials(sysConfig["rabbit"]["user"],sysConfig["rabbit"]["password"])
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq",5672,'/',credentials))
    channel = connection.channel()
    data = request.json
    if data["concierto"] and data["mensaje"]:
        try:
            model.queueUp(sysConfig[data["concierto"]],clean(data["mensaje"]), channel, logger)
            return "Encolado"
        except:
            model.queueUp(sysConfig["Otros"],clean(data["mensaje"]), channel, logger)
            return "Encolado"
    else:
        print('Parametros incorrectos.')
        return "No encolado"
