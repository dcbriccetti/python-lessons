import string
from random import randint, choice
from flask import Flask, abort
app = Flask(__name__)

URL_BASE = "http://192.168.1.7:5000/"


def path_gen():
    chars = string.ascii_lowercase + string.digits
    while True:
        yield ''.join([choice(chars) for a in range(5)])

multiplier = randint(1, 10)
multiplicand = randint(1, 10)
actual_product = multiplier * multiplicand
rg = path_gen()
max_puzzle_path = next(rg)
treasure = str(1000 + randint(0, 999))
max_of = [3000 + randint(0, 999) for n in range(500)]
largest = str(max(max_of))
max_of_str = [str(n) for n in max_of]


def u(p): return URL_BASE + p


@app.route("/")
def start():
    return "%s where number = %s × %s" % (u("number"), u('multiplier'), u('multiplicand'))


@app.route('/multiplier')
def m1():
    return str(multiplier)


@app.route('/multiplicand')
def m2():
    return str(multiplicand)


@app.route("/" + max_puzzle_path)
def max_puzzle():
    return "%s where number is the largest of (%s)" % (u('number'), ', '.join(max_of_str))


@app.route("/<int:product_guess>")
def product(product_guess):
    return u(max_puzzle_path) if product_guess == actual_product else abort(404)


@app.route("/" + largest)
def words_matching_regex():
    return '%s where string is the word from this list with three vowels in a row: (kidnapper, bindweed, euonymus, almost, marabou, dismembered, underused, struma, assumptions, tzar, naze, wore, bare, jones, stick, zebrine, laxative, reynard, uninjured, river, manners, faulty, neglect, required, shabby, lobster, dour, fraise, colognes, expressing, eardrop, sneaker, adultery)' % \
        u("string")


@app.route("/euonymus")
def treasure():
    return "You have reached the treasure!"


if __name__ == "__main__":
    app.run(host='192.168.1.7', debug=True)