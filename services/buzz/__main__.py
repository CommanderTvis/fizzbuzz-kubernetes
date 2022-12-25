import os

import waitress
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))
m = int(os.getenv("M", default=5))


@app.get("/buzz/")
def buzz() -> Response:
    try:
        variable = int(request.args.get("value"))
    except (ValueError, TypeError):
        return jsonify(error="Expected integer parameter 'value'")

    if variable % m == 0:
        return jsonify(result="buzz")
    return jsonify(result="")


waitress.serve(app, host=host, port=port)
