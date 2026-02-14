import logging

from flask import Flask, jsonify, request

from calculadora.logic import add, divide, multiply, subtract

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Calculadora API - Suma, Resta, Multiplicacion y Division",
            "status": "ok",
        }
    )


@app.route("/add", methods=["POST"])
def do_add():
    data = request.get_json()
    result = add(data["a"], data["b"])
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def do_subtract():
    data = request.get_json()
    result = subtract(data["a"], data["b"])
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def do_multiply():
    data = request.get_json()
    result = multiply(data["a"], data["b"])
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def do_divide():
    data = request.get_json()
    try:
        result = divide(data["a"], data["b"])
        return jsonify({"result": result})
    except ValueError:
        app.logger.exception("Error while performing division")
        return jsonify({"error": "Invalid input for division."}), 400
