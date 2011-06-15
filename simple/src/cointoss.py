import random

# Ask the user how many tosses to make and store the answer in numTosses
numTosses = int(input('How many tosses? '))

# Loop "numTosses" times
numHeads = 0
numTails = 0
for t in range(numTosses):
    if random.random() < .5:
        numHeads += 1
    else:
        numTails += 1
        
print('There were ' + str(numHeads) + ' heads and ' + str(numTails) + ' tails')

