
from flask import Flask, request, jsonify, json
from common import *

from controller import tokens


def run_app():
    app.run(host=sysConfig["host"],
            port=sysConfig["port"], debug=True, threaded=True)
