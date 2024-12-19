from flask import Flask, request, jsonify
from utils import *

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
    app.run(debug=True, port=5000)