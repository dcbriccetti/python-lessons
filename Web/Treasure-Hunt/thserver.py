from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "You have reached the treasure!"


@app.route("/n-1")
def n1():
    return "http://localhost:5000/"


@app.route("/n-2")
def n2():
    return "http://localhost:5000/n-1"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)