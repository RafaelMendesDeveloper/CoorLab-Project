from flask import Flask, request, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data.json'))

with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/api/transport', methods=['GET'])
def get_transport_by_city():
    city = request.args.get('city')
    print('Cidade selecionada:', city)
    filtered_transport = [t for t in data['transport'] if t['city'] == city]
    print('Transporte filtrado:', filtered_transport)
    if not filtered_transport:
        print('Nenhum transporte encontrado para a cidade:', city)
        return jsonify([]), 404
    return jsonify(filtered_transport)

@app.route('/')
def index():
    return 'Bem-vindo ao meu servidor Flask!'


@app.route('/api/cities', methods=['GET'])
def get_cities():
    cities = [t['city'] for t in data['transport']]
    unique_cities = list(set(cities))
    return jsonify(unique_cities)

if __name__ == '__main__':
    app.run(debug=True)
