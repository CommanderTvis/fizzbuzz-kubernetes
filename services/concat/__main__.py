import os

from flask import Flask, request, jsonify

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))


@app.get("/concat/")
def concat():
    lhs = request.args.get("lhs")
    if lhs is None:
        return jsonify(error="Expected string parameter 'lhs'")
    rhs = request.args.get("rhs")
    if rhs is None:
        return jsonify(error="Expected string parameter 'rhs'")
    return jsonify(result=lhs + rhs)


app.run(host=host, port=port)
