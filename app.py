from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "This is index page"


@app.route("/sum2/<a>/<b>", methods=["GET"])
def summer(a, b):
    a = int(a) * 2
    b = int(b)

    sum2 = sum([a, b])
    return {"sum": sum2}


@app.route("/text/<name>/<int:age>", methods=["GET"])
def text(name, age):

    n = str(name)
    a = int(age)

    return f"this is your {n} and this is ur age {a}"


if __name__ == "__main__":
    app.run()
