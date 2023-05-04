from flask import Flask, json
import time,sys
from flask_cors import CORS, cross_origin


def read_config():

    if len(sys.argv) < 2:
        print("error, debe ingresar el nombre del archivo de configuracion")
        sys.exit(1)

    configFile = sys.argv[1]

    data = ""
    with open(configFile) as json_file:
        data = json.load(json_file)
    return  data
###############################################################################

#CONSTANTE DEL SISTEMA
app = Flask(__name__)
CORS(app)
sysConfig = read_config()