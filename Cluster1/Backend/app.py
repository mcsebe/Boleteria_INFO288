#!/usr/bin/env python
from flask import Flask, request, jsonify, json
from common import *
import model
from datetime import datetime, timedelta

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)

# Abriendo el log de eventos
format = "%H:%M:%S;%d/%m/%Y"
wFile = os.getcwd() + "\\Log\\" + "logs.txt"
try:
    file = open(wFile, 'a+')
except:
    logs = os.getcwd() + "/files/" + "logs.txt"
    file = open(logs, 'a+')


# Ruta que entrega la información del concierto: Capacidad, Asientos disponibles e información general presente en la base de datos
@app.route('/informacion', methods=['GET', 'PUT'])
def getInformation():
    concert = int(request.json["Id"])
    total = set(range(1, model.capacity(
        sysConfig["dbConnConfig"], concert)[0] + 1))
    taken = set(model.available(sysConfig["dbConnConfig"], concert))

    # Escribe en el log de eventos
    current_time = datetime.now()
    current_time_formated = current_time.strftime(format)
    file.write(current_time_formated +
               "; Consulta sobre información;" + str(concert) + "\n")


    return [list(total - taken)] + [model.information(sysConfig["dbConnConfig"], concert)] + [model.location(sysConfig["dbConnConfig"], concert)]

# Ruta que envia los datos del formulario a la base de Datos
@app.route('/subir', methods=['POST'])
def createReservation():
    data = request.json
    return model.insert(sysConfig["dbConnConfig"], sysConfig["dbConnConfig2"], data, format, file)
