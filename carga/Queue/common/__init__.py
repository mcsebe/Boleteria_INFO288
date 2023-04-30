from flask import Flask, json
import sys

# Función que lee los argumentos y asigna los valores del config.json correspondiente a la variable sysConfig
def read_config():

    if len(sys.argv) < 2:
        print("error, debe ingresar el nombre del archivo de configuracion")
        sys.exit(1)

    configFile = sys.argv[1]

    data = ""
    with open(configFile) as json_file:
        data = json.load(json_file)
    return  data


app = Flask(__name__)
sysConfig = read_config()