from flask import Flask, request, jsonify, json, redirect, render_template
from common import app, sysConfig
from controller import *
import model
from http import cookies
import time


@app.route('/token', methods=['GET', 'PUT'])
def Token():
    r = request.get_json()
    print("hola")
    tokenid = r["mensaje"]
    if tokenid:
        if ("123" == tokenid):  # sysConfig["dbConnConfig"]
            print("verda")
            return ("v")
        else:
            print("falso")
            time.sleep(10)
            return redirect('/token')
    else:
        print("no hay token")
        time.sleep(10)
        return redirect('/')


@app.route('/concierto/<int:id>')
def PaginaDePago():
    r = request.get_json()
    tokenid = r["mensaje"]
    if tokenid:
        if (model.token("123", tokenid)):  # sysConfig["dbConnConfig"]
            return render_template('')
        else:
            time.sleep(10)
            return redirect('/')
    else:
        time.sleep(10)
        return redirect('/')
