from flask import Flask, request
from common import app, sysConfig
from controller import *
import model
import os

# Variable que se utilizará
format = "%H:%M:%S;%d/%m/%Y"

# Ruta para consultar si el token se encuentra en la base de datos
@app.route('/token', methods=['GET', 'PUT'])
def Token():
    token = request.json["Token"]
    if token:
        return model.token(sysConfig["dbConnConfig"],token, sysConfig["server_name"], format)
    else:
        return "NO"