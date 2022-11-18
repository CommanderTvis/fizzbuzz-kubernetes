from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def concat():
    lhs = str(request.args.get("lhs"))
    rhs = str(request.args.get("rhs"))
    return lhs + rhs


app.run()
