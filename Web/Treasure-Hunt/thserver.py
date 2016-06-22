'''
A simple treasure hunt server.
/ -> /garden -> /shed -> /attic
'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def start():
    return '/garden'


@app.route('/garden')
def garden():
    return '/shed'


@app.route('/shed')
def shed():
    return '/attic'


@app.route('/attic')
def attic():
    return "You have reached the treasure!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)