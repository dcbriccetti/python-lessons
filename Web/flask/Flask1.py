import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Here is the top page."

@app.route("/hello")
def hello():
    return "Hello World! What’s new?"

@app.route("/time")
def show_time():
    return "The time is now %s" % time.time()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
