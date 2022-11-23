from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultados import ControladorResultados
miControladorCandidato=ControladorCandidato()
miControladorPartido=ControladorPartido()
miControladorMesa=ControladorMesa()
miControladorresultados=ControladorResultados()

############################################

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###########################################

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesas():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:mesa>",methods=['GET'])
def getMesa(mesa):
    json=miControladorMesa.show(mesa)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesas(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

################################################

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorresultados.index()
    return jsonify(json)
@app.route("/resultados",methods=['POST'])
def crearResultados():
    data = request.get_json()
    json=miControladorresultados.create(data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorresultados.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json=miControladorresultados.update(id,data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultados(id):
    json=miControladorresultados.delete(id)
    return jsonify(json)

"relaciones"
@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json = miControladorresultados.createResultado(data,id_candidato,id_mesa)
    return jsonify(json)
#####################################################################
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
####################################################################
@app.route("/partido",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
###################################################################
"relaciones"
@app.route("/candidato/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def AsignarPartidoACandidato(id, id_partido):
    json=miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)

###################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])