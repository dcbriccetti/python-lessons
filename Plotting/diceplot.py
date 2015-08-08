from random import randint
import matplotlib.pyplot as plt
import numpy as np

def getThrow(maxValue):
    return randint(1, maxValue)

numDice = 3
numDiceSides = 6
numThrows = 1000
maxDiceSum = numDiceSides * numDice
throws = np.zeros(maxDiceSum)
ys = np.arange(1, maxDiceSum + 1)

for t in range(numThrows):
    throwSum = 0
    for s in range(numDice):
        throwSum += getThrow(numDiceSides)
    throws[throwSum - 1] += 1

plt.barh(ys, throws, align='center', alpha=0.4)
plt.xlabel('Number of each outcome')
plt.ylabel('Outcome (Sum of Die Values)')
dieOrDice = "Die" if numDice == 1 else "Dice"
plt.title('%s Throw Simulation—%d %d-Sided %s' %
    (dieOrDice, numDice, numDiceSides, dieOrDice))
plt.show()
