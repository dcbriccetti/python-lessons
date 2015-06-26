import math

print("""
This program calculates how far your bike moved,
given the wheel size and number of turns of the
wheel.
""")

diam = float(eval(input("What is the diameter of your front wheel (in meters)? ")))

# To calculate the circumference from the diameter, multiply by pi
circ = diam * math.pi

turns = float(eval(input("How many times did it turn? ")))

# Each turn the bike moves forward by the circumference
dist = circ * turns

print(('The circumference of your wheel is %.2f meters.' % (circ)))
print(('The bike travelled %.2f meters.' % dist))
