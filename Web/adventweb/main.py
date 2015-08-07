from flask import Flask, render_template, redirect
from place import Place
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(place.path)

@app.route("/<newPath>")
def show_place(newPath):
    global place
    newDest = places_by_path.get(newPath)
    if newDest in transitions[place]:
        place = newDest
    return render_template("advent.html", place=place, destinations=transitions[place])

pumpkin = Place('pumpkin', 'Arduino-Powered Pumpkin')
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
place = pumpkin

app.secret_key = 'the dog flies at noon'
app.run()
