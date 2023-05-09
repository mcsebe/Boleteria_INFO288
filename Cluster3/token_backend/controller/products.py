from flask import Flask, request, jsonify, json, redirect, render_template
from common import app, sysConfig
from controller import *
import model
from http import cookies
import time


@app.route('/token', methods=['GET', 'PUT'])
def Token():
    token = request.json["Token"]
    if token:
        return model.token(sysConfig["dbConnConfig"],token, sysConfig["server_name"])
    else:
        return "NO"