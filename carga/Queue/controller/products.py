from flask import Flask, request, jsonify,json
from common import app, sysConfig
from controller import *
import model 

@app.route('/query', methods=['GET']) 
def getProducts():
    # Lee los argumentos de productos y categorias
    productos = request.args.get('productos')
    categoria = request.args.get('categoria')
    # Si se puso el argumento de productos, entonces llama al método select_productos
    if productos:
        productos = productos.split(" ")
        return model.select_productos(sysConfig["archivo"], productos)
    
    # Si se puso el argumento de categorias, entonces llama al método select_categoria
    elif categoria:
        return model.select_categoria(sysConfig["archivo"])
        
    else:
        return 'Parametros incorrectos.'
