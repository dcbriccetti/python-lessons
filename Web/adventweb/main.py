from flask import Flask, render_template, redirect, session
from place import Place

STARTING_PLACE_INDEX = 0
app = Flask(__name__)

@app.route("/")
def index():
    session['placeIndex'] = STARTING_PLACE_INDEX
    return redirect(places[STARTING_PLACE_INDEX].path)

@app.route("/<newPath>")
def show_place(newPath):
    placeIndex = session.get('placeIndex', STARTING_PLACE_INDEX)
    place = places[placeIndex]
    newDest = places_by_path.get(newPath)
    if newDest in transitions[place]:
        place = newDest
        session['placeIndex'] = places.index(place)
    return render_template("advent.html", place=place, destinations=transitions[place])

pumpkin = Place('pumpkin', 'Arduino-Powered Pumpkin', audio='135498__compusician__halloween-003-wav-120b.wav')
monster = Place('monster', 'Flying Spaghetti Monster')
camera  = Place('camera',  'Government Spy Camera')
trail   = Place('trail',   'Mountain Bike Trail')

places = (pumpkin, monster, camera, trail)
places_by_path = {p.path: p for p in places}

transitions = {
    pumpkin: (monster,),
    monster: (pumpkin, camera),
    camera : (monster, trail),
    trail  : (camera,),
}

app.secret_key = 'the dog flies at noon'
app.run()
