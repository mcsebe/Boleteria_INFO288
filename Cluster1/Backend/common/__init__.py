from flask import Flask, json
import sys, os


# Abre el archivo config.json, para que se pueda acceder mediante la variable sysConfig
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
    

app = Flask(__name__)
sysConfig = read_config()