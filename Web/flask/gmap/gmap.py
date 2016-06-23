from flask import Flask, render_template, abort
app = Flask(__name__)

schools = {
    'hv':       ('Happy Valley',    37.905,     -122.1445),
    'stanley':  ('Stanley',         37.8862125, -122.1148579)
}


@app.route("/")
def index():
    return "Try /stanley or /hv"


@app.route("/<school_code>")
def show_school(school_code):
    school = schools.get(school_code)
    if school:
        return render_template('map.html', lat=school[1], lng=school[2], school=school[0])
    else:
        abort(404)

app.run(host='0.0.0.0', port=8001, debug=True)
