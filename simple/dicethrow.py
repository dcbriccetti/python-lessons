'''Simulates throwing a die.'''

from random import randint

numSides = 10
numThrows = 100

for t in range(numThrows):
    print(randint(1, numSides))
