from flask import Flask, render_template
app = Flask(__name__)

school_codes = {
    'hv': 'Happy Valley',
    'stanley': 'Stanley'
}

@app.route("/")
def index():
    return "Try /stanley or /hv"

@app.route("/<school_code>")
def school(school_code):
    if school_code == 'stanley':
        return render_template('map.html', lat=37.8862125, lng=-122.1148579, school=school_codes[school_code])
    elif school_code == 'hv':
        return render_template('map.html', lat=37.905, lng=-122.1445, school=school_codes[school_code])

app.run(host='0.0.0.0', debug=True)
