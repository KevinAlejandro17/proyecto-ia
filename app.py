from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from .algorithms.utils import load_world, encontrar_estado_inicial
from .algorithms.amplitud import amplitud
from .algorithms.costo import costo_uniforme


app = Flask(__name__)

cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

world_file_path = "app/resources/mundo.txt"
world = load_world(world_file_path)

estado_inicial = encontrar_estado_inicial(world)

@app.route('/amplitud', methods=['GET'])
@cross_origin()
def busqueda_por_amplitud():
    try:
        ruta, profundidad, expandidos_con_padre = amplitud(world, estado_inicial)
        response = jsonify(ruta)  
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/costo', methods=['GET'])
@cross_origin()
def cost():
    try:
        ruta, expandidos_con_padre = costo_uniforme(world, estado_inicial)
        response = jsonify(ruta)  
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500
