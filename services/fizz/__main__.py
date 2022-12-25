import os

from flask import Flask, request, jsonify

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))
n = int(os.getenv("N", default=3))


@app.get("/fizz/")
def fizz():
    try:
        variable = int(request.args.get("value"))
    except (ValueError, TypeError):
        return "Expected integer parameter 'value'"

    if variable % n == 0:
        return jsonify(result="fizz")
    return jsonify(result="")


app.run(host=host, port=port)
