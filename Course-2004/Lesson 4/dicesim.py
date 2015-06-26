import random

def getThrow(maxValue):
    return random.randrange(1, maxValue + 1)

throws = {}
diceSides = 6
numDice = 5
numThrows = 100
maxDiceSum = diceSides * numDice

for n in range(1, maxDiceSum + 1):
    throws[n] = 0

for t in range(numThrows):
    throwSum = 0
    for s in range(numDice):
        throwSum += getThrow(diceSides)
    throws[throwSum] += 1

for n in range(numDice, maxDiceSum + 1):
    print(("%2d" % n, 'X' * throws[n]))
