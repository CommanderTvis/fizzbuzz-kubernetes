import os

from flask import Flask, request, jsonify

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))
m = int(os.getenv("M", default=5))


@app.get("/buzz/")
def buzz():
    try:
        variable = int(request.args.get("value"))
    except (ValueError, TypeError):
        return "Expected integer parameter 'value'"

    if variable % m == 0:
        return jsonify(result="buzz")
    return jsonify(result="")


app.run(host=host, port=port)
