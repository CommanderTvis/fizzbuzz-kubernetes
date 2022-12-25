import os

import requests as requests
from flask import Flask, request, jsonify

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))
fizz_host = os.getenv("FIZZ_HOST")
buzz_host = os.getenv("BUZZ_HOST")
concat_host = os.getenv("CONCAT_HOST")


@app.post("/")
def main():
    try:
        value = int(request.get_json()["value"])
    except (ValueError, TypeError):
        return "Expected integer parameter 'value'"
    print(requests.get(fizz_host + "/fizz", params={"value": value}))
    print(requests.get(fizz_host + "/buzz", params={"value": value}))
    fizz = requests.get(fizz_host + "/fizz", params={"value": value}).json()["result"]
    buzz = requests.get(buzz_host + "/buzz", params={"value": value}).json()["result"]
    concat = requests.get(concat_host + "/concat", params={"lhs": fizz, "rhs": buzz}).json()["result"]
    return jsonify(result=concat)


app.run(host=host, port=port)
