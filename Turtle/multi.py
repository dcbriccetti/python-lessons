import turtle
from random import randint
turtle.speed('fast')

turtles = [turtle.Turtle() for n in range(5)]

for n in range(10):
    for turtle in turtles:
        turtle.forward(randint(50, 100))
        turtle.right(randint(85, 95))
