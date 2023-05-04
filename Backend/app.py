#!/usr/bin/env python
from flask import Flask, request, jsonify,json
from common import *
import model

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.run(debug=True)

@app.route('/informacion', methods=['GET', 'PUT']) 
def getInformacion():
    concierto = int(request.json["Id"])
    total = set(range(1, model.capacidad(sysConfig["dbConnConfig"], concierto)[0] + 1))
    ocupados = set(model.disponible(sysConfig["dbConnConfig"], concierto))
    return [list(total - ocupados)] + [model.informacion(sysConfig["dbConnConfig"], concierto)] + [model.localizacion(sysConfig["dbConnConfig"], concierto)]


@app.route('/subir', methods=['POST']) 
def createReserva():
    data = request.json
    return model.insert(sysConfig["dbConnConfig"], sysConfig["dbConnConfig2"], data)