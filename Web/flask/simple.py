from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hi from a webapp!"

app.run(host='0.0.0.0', debug=True)
