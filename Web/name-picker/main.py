from flask import Flask, render_template, redirect
from random import randint

app = Flask(__name__)
allNames = ('Jim', 'Sue', 'Steve') * 5
names = list(allNames)

@app.route("/")
def index():
    global names
    if names:
        name = names.pop(randint(0, len(names) - 1))
        return render_template("names.html", name=name)
    else:
        return render_template("empty.html")

@app.route("/reset")
def reset():
    global names
    names = list(allNames)
    return redirect("/")

app.run(debug=True)
