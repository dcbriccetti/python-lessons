from random import choice
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    fortune = choice(
        'You will have good health',
        'You will not have good health'
    )
    return render_template('simple2.html', fortune=fortune)

app.run(host='127.0.0.1', debug=True)
