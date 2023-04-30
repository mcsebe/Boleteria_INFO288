
from flask import Flask, request, jsonify,json
from common import *

from controller import products

#lanza la app
def run_app():
    app.run(host = sysConfig["host"], port = sysConfig["port"],debug=True, threaded=True)

