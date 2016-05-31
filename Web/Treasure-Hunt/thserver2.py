from random import randint
from flask import Flask
app = Flask(__name__)

url_base = "http://192.168.1.7:5000/"
mlt1 = randint(1, 10)
mlt2 = randint(1, 10)
product = mlt1 * mlt2
treasure = str(1000 + randint(0, 999))
max_puzzle_nums = str(2000 + randint(0, 999))
max_of = [3000 + randint(0, 999) for n in range(500)]
largest = str(max(max_of))
max_of_str = [str(n) for n in max_of]


def u(p): return url_base + p

@app.route("/")
def start():
    return "%s where number = %s * %s" % (u("number"), u("m1"), u("m2"))


@app.route("/m1")
def m1():
    return str(mlt1)


@app.route("/m2")
def m2():
    return str(mlt2)


@app.route("/" + str(product))
def product():
    return u(max_puzzle_nums)


@app.route("/" + max_puzzle_nums)
def max_puzzle():
    return "%s where number is the largest of (%s)" % (u("number"), ",".join(max_of_str))


@app.route("/" + largest)
def words_matching_regex():
    return '%s where string is the word from this list with three vowels in a row: (kidnapper,bindweed,euonymus,almost,marabou,dismembered,underused,struma,assumptions,tzar,naze,wore,bare,jones,stick,zebrine,laxative,reynard,uninjured,river,manners,faulty,neglect,required,shabby,lobster,dour,fraise,colognes,expressing,eardrop,sneaker,adultery)' % \
        u("string")


@app.route("/euonymus")
def treasure():
    return "You have reached the treasure!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)