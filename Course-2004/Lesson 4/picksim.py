import random

def getPick():
    return random.choice(("bananas", "turnips", "radishes", "papayas"))

picks = {}
numPicks = 100

for t in range(numPicks):
    pick = getPick()
    if pick in picks:
        picks[pick] += 1
    else:
        picks[pick] = 1

for n in list(picks.keys()):
    print(("%10s" % n, 'X' * picks[n]))
    
