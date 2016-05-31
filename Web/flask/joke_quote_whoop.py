from random import choice, randint
from flask import Flask, request
app = Flask(__name__)
quotes = (
    'Computer science is no more about computers than astronomy is about telescopes. - Edsger Dijkstra',
    'People think that computer science is the art of geniuses but the actual reality is the opposite, ' +
        'just many people doing things that build on each other, like a wall of mini stones. - Donald Knuth',
    'Programs must be written for people to read, and only incidentally for machines to execute. - H. Abelson and G. Sussman',
    "I don't know how many of you have ever met Dijkstra, but you probably know that arrogance in computer science is measured in nano-Dijkstras. - Alan Kay"
)
jokes = (
    'What does the chemist say when he finds two helium molecules? HeHe.',
    # Add some jokes here
)

@app.route("/")
def index():
    return "Hi %s. Try /joke, /quote, or /whoop." % request.remote_addr

@app.route("/joke")
def joke():
    return choice(jokes)

@app.route("/quote")
def quote():
    return choice(quotes)

@app.route("/whoop")
def whoop():
    return "whoop " * randint(1, 20)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
