import os

from flask import Flask, request

app = Flask(__name__)

n = int(os.getenv("N", default=3))


@app.get("/")
def fizz():
    try:
        variable = int(request.args.get("value"))
    except (ValueError, TypeError):
        return "Expected integer parameter 'value'"

    if variable % n == 0:
        return "fizz"
    return ""


app.run()
