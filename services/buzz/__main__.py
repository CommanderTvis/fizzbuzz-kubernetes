import os

from flask import Flask, request

app = Flask(__name__)

m = int(os.getenv("M", default=5))


@app.get("/")
def buzz():
    try:
        variable = int(request.args.get("value"))
    except (ValueError, TypeError):
        return "Expected integer parameter 'value'"

    if variable % m == 0:
        return "buzz"
    return ""


app.run()
