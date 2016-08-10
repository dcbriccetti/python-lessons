from flask import Flask, render_template, redirect
from random import randint

HOW_MANY_OF_EACH_NAME = 3
all_names = ('John Mary Sue'.split(' ')) * HOW_MANY_OF_EACH_NAME
remaining_names = list(all_names)

app = Flask(__name__)


@app.route("/")
def index():
    if remaining_names:
        name = remaining_names.pop(randint(0, len(remaining_names) - 1))
        return render_template("names.html", name=name, remaining=len(remaining_names))
    else:
        return redirect("/reset")


@app.route("/reset")
def reset():
    global remaining_names
    remaining_names = list(all_names)
    return redirect("/")

app.run(debug=True, port=8181)
