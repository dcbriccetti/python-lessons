from xturtle import *

pensize(3)
color('blue')
sides = int(raw_input('How many sides? '))
for n in range(sides):
    fd(20)
    rt(360 / sides)

raw_input('Continue')

    
