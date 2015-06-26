import math
diameter = float(input('Diameter of bike wheel in inches?'))
rotate = int(input('How many rotations did the bike turn?'))
dist = diameter * math.pi * rotate
print('The bike travelled %.0f inches' % dist)
