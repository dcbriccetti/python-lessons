import turtle as t
from time import sleep

t.speed('fastest')
for num_sides in range(3, 11):
    for n in range(num_sides):
        t.fd(50)
        t.rt(360 / num_sides)

sleep(2)