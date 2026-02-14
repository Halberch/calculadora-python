import logging
import time

from flask import Flask, g, jsonify, request

from calculadora.logic import add, divide, multiply, subtract

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)


@app.before_request
def log_request_start():
    g.start_time = time.time()
    app.logger.info(
        "REQUEST START method=%s path=%s payload=%s",
        request.method,
        request.path,
        request.get_json(silent=True),
    )


@app.after_request
def log_request_end(response):
    duration_ms = (time.time() - g.start_time) * 1000
    app.logger.info(
        "REQUEST END method=%s path=%s status=%s duration_ms=%.2f",
        request.method,
        request.path,
        response.status_code,
        duration_ms,
    )
    return response


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
    app.logger.info("ADD a=%s b=%s result=%s", data["a"], data["b"], result)
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def do_subtract():
    data = request.get_json()
    result = subtract(data["a"], data["b"])
    app.logger.info("SUBTRACT a=%s b=%s result=%s", data["a"], data["b"], result)
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def do_multiply():
    data = request.get_json()
    result = multiply(data["a"], data["b"])
    app.logger.info("MULTIPLY a=%s b=%s result=%s", data["a"], data["b"], result)
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def do_divide():
    data = request.get_json()
    try:
        result = divide(data["a"], data["b"])
        app.logger.info("DIVIDE a=%s b=%s result=%s", data["a"], data["b"], result)
        return jsonify({"result": result})
    except ValueError:
        app.logger.exception("Error while performing division")
        return jsonify({"error": "Invalid input for division."}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
