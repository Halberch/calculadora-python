from flask import Flask, request, jsonify
from logic import add, subtract

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Calculadora API - Suma y Resta", "status": "ok"})

@app.route('/add', methods=['POST'])
def do_add():
    data = request.get_json()
    result = add(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def do_subtract():
    data = request.get_json()
    result = subtract(data['a'], data['b'])
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)