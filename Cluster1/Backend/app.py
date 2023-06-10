#!/usr/bin/env python
from flask import Flask, request, jsonify, json
from common import *
import model
from datetime import datetime, timedelta
import logging
from flask_cors import CORS, cross_origin
import re

app = Flask(__name__)
CORS(app)
app.run(debug=True)
print("????")
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
logging.getLogger("pika").propagate = False
print("?")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(sysConfig["log_rute"])
handler.setFormatter(logging.Formatter('%(asctime)s;%(message)s', datefmt="%H:%M:%S;%d/%m/%Y"))
logger.addHandler(handler)

def clean(unverified_input):
    return(re.sub(r'[\'";]', '', unverified_input))
# Ruta que entrega la información del concierto: Capacidad, Asientos disponibles e información general presente en la base de datos
@app.route('/informacion', methods=['GET', 'PUT'])
def getInformation():
    concert = int(request.json["Id"])
    
    # Escribe en el log de eventos
    logger.info("Consulta sobre información;" + str(concert))

    return [model.available(sysConfig["dbConnConfig"], concert)] + [model.information(sysConfig["dbConnConfig"], concert)] + [model.location(sysConfig["dbConnConfig"], concert)]

# Ruta que envia los datos del formulario a la base de Datos
@app.route('/subir', methods=['POST'])
def createReservation():
    data = request.json
    return model.insert(sysConfig["dbConnConfig"], sysConfig["dbConnConfig2"], data, logger, sysConfig["rabbit"])
