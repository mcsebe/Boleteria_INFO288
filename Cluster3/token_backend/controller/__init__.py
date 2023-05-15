
from flask import Flask, request, jsonify, json
from common import *


def run_app():
    app.run(host=sysConfig["host"],
            port=sysConfig["port"], debug=True, threaded=True)
