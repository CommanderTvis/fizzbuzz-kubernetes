import os

import waitress
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))


@app.get("/concat/")
def concat() -> Response:
    lhs = request.args.get("lhs")
    if lhs is None:
        return jsonify(error="Expected string parameter 'lhs'")
    rhs = request.args.get("rhs")
    if rhs is None:
        return jsonify(error="Expected string parameter 'rhs'")
    return jsonify(result=lhs + rhs)


waitress.serve(app, host=host, port=port)
