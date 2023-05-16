from flask import Flask, json
import os
import time,sys


def read_config():
    # Obtiene la ruta actual
    d = os.getcwd()
    try:
        # Ruta en Windows
        configFile = d + "\\config\\config.json"
        data = ""
        with open(configFile) as json_file:
            data = json.load(json_file)
        return  data
    except:
        # Ruta en Linux
        configFile = d + "/config/config.json"
        data = ""
        with open(configFile) as json_file:
            data = json.load(json_file)
        return  data
    

#CONSTANTE DEL SISTEMA
app = Flask(__name__)
sysConnConfig = read_config()