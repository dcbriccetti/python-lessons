import turtle as t
from random import choice
from time import sleep

colors = ('red', 'green', 'blue', 'yellow', 'black')
t.speed('fastest')
t.pu()
t.goto(400, -100)
t.setheading(90)
t.pd()
t.pensize(10)
turn = 10
length = 100
while length > 20:
    t.color(choice(colors))
    t.fd(length)
    t.left(turn)
    turn += 0.1
    length *= 0.99

sleep(1000)