from flask import Flask, json
import os
import time,sys


def read_config():
    configFile = os.getcwd() + "\\config\\config.json"

    data = ""
    with open(configFile) as json_file:
        data = json.load(json_file)
    return  data
###############################################################################

#CONSTANTE DEL SISTEMA
app = Flask(__name__)
dbConnConfig = read_config()