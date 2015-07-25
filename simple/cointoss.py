from random import randint

# Ask the user how many tosses to make and store the answer in numTosses
numTosses = int(input('How many tosses? '))

numHeads = 0
numTails = 0

# Loop "numTosses" times
for t in range(numTosses):
    if randint(1, 2) == 1:
        numHeads += 1
    else:
        numTails += 1
        
print('There were %s heads and %s tails' % (numHeads, numTails))
