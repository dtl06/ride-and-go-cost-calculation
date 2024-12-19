from flask import Flask, request, jsonify
from utils import *
import os

app = Flask(__name__)

@app.route('/cost', methods=['POST'])
def cost():
    data = request.get_json()
    data = get_data(data.get('start'), data.get('end'),data.get('hour'))
    cost = calculate_cost(data)
    # return jsonify({'cost':cost})
    return f"{cost}"
    
def calculate_cost(data):
    return model.predict(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render définit le port via la variable d'environnement PORT
    app.run(host="0.0.0.0", port=port)        # Assure-toi d'utiliser host="0.0.0.0" pour accepter les connexions externes
