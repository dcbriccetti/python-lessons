from flask import Flask, render_template, abort
app = Flask(__name__)


class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('hv',      'Happy Valley Elementary', 37.905, -122.1445),
    School('stanley', 'Stanley Middle',          37.886, -122.1149)
)
schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    return render_template('index.html', schools=schools)


@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)

app.run(host='0.0.0.0', port=8001, debug=True)
