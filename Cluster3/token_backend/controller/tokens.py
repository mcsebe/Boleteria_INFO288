from flask import Flask, request
from common import app, sysConfig
from controller import *
import model
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(sysConfig["log_rute"])
handler.setFormatter(logging.Formatter('%(asctime)s;%(message)s', datefmt="%H:%M:%S;%d/%m/%Y"))
logger.addHandler(handler)

# Ruta para consultar si el token se encuentra en la base de datos
@app.route('/token', methods=['GET', 'PUT'])
def Token():
    token = request.json["Token"]
    if token:
        return model.token(sysConfig["dbConnConfig"],token, sysConfig["server_name"], logger)
    else:
        return "NO"