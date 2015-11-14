import time
from flask import Flask
from random import choice, randint
app = Flask(__name__)
jokes = ('Whoop whoop whoop whoop whoop', 'To get to the other side')

@app.route("/")
def index():
    return "Here is the top page."

@app.route("/joke")
def joke():
    return choice(jokes)

@app.route("/whoop")
def whoop():
    return "whoop " * randint(1, 10)

@app.route("/hello")
def hello():
    return "Hello World! What’s new?"

@app.route("/time")
def show_time():
    return "The time is now %s" % time.time()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
