'''Simulates throwing a die.'''

from random import randint

numSides = 6
numThrows = 10

for t in range(numThrows):
    print(randint(1, numSides))

input('Press a key to continue')
