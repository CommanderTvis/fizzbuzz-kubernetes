import os

import request_boost
import requests as requests
import waitress
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
host = os.getenv("HOST", default="0.0.0.0")
port = int(os.getenv("PORT", default="5000"))
fizz_host = os.getenv("FIZZ_HOST")
buzz_host = os.getenv("BUZZ_HOST")
concat_host = os.getenv("CONCAT_HOST")


@app.post("/fizzbuzz/")
def main() -> Response:
    try:
        value = int(request.get_json()["value"])
    except (ValueError, TypeError):
        return jsonify(error="Expected integer parameter 'value'")

    urls = [f"{fizz_host}/fizz/?value={value}", f"{buzz_host}/buzz/?value={value}"]
    results = request_boost.boosted_requests(urls=urls, no_workers=2, max_tries=1, verbose=True)
    fizz, buzz = results
    concat = requests.get(concat_host + "/concat/", params={"lhs": fizz["result"], "rhs": buzz["result"]}).json()[
        "result"]
    return jsonify(result=concat)


waitress.serve(app, host=host, port=port)
