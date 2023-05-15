#!/usr/bin/env python
from flask import Flask, request, jsonify,json
from common import *
import model
from datetime import datetime, timedelta

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)

# Ruta que entrega la información del concierto: Capacidad, Asientos disponibles e información general presente en la base de datos
@app.route('/informacion', methods=['GET', 'PUT']) 
def getInformacion():
    concierto = int(request.json["Id"])
    total = set(range(1, model.capacidad(sysConfig["dbConnConfig"], concierto)[0] + 1))
    ocupados = set(model.disponible(sysConfig["dbConnConfig"], concierto))

    # Escribe en el log de eventos
    # ----------------------------------------------------------------------------
    fecha_hora_actual = datetime.now()
    formato = "%H:%M:%S;%d/%m/%Y"
    fecha_hora_formateada = fecha_hora_actual.strftime(formato)

    #Ruta en windows
    archivoW = os.getcwd() + "\\Log\\"+ "logs.txt"
    try:
        file = open(archivoW, 'a+')
    #Ruta en linux
    except:
        archivoL = os.getcwd() + "/files/"+ "logs.txt"
        file = open(archivoL, 'a+')

    file.write(fecha_hora_formateada + "; Consulta sobre información;" + str(concierto) + "\n")
    file.close()
    # ----------------------------------------------------------------------------

    return [list(total - ocupados)] + [model.informacion(sysConfig["dbConnConfig"], concierto)] + [model.localizacion(sysConfig["dbConnConfig"], concierto)]

# Ruta que envpia los datos del formulario a la base de Datos
@app.route('/subir', methods=['POST']) 
def createReserva():
    data = request.json
    return model.insert(sysConfig["dbConnConfig"], sysConfig["dbConnConfig2"], data)