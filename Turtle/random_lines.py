from sys import exit
import turtle as t
from random import randint, choice

colors = ('blue', 'red', 'green', 'yellow')
t.speed('fastest')
t.pensize(20)
while True:
    t.color(choice(colors))
    t.fd(randint(20, 200))
    t.rt(randint(-45, 45))
    if abs(t.pos()[0]) > 500 or abs(t.pos()[1]) > 500:
        t.setpos((randint(-100, 100), (randint(-100, 100))))
