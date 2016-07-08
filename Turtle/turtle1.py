from time import sleep
import turtle as t

for sides in range(3, 6):
    for side in range(sides):
        t.fd(100)
        t.right(360 / sides)

sleep(2)
