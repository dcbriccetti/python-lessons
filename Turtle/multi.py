from turtle import speed, Turtle
from random import randint
speed('fast')

turtles = [Turtle() for n in range(5)]

for n in range(10):
    for t in turtles:
        t.forward(randint(50, 100))
        t.right(randint(85, 95))
