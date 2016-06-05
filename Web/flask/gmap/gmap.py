from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/stanley")
def index():
    return render_template('map.html', lat=37.8862125, lng=-122.1148579)

app.run(host='0.0.0.0', debug=True)
