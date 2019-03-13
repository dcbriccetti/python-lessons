from random import randint
import matplotlib.pyplot as plt
import numpy as np

DICE = 2
SIDES = 6
THROWS = 1000

highest_outcome = SIDES * DICE
outcome_counts = np.zeros(highest_outcome)
ys = np.arange(1, highest_outcome + 1)

for t in range(THROWS):
    throw_sum = sum((randint(1, SIDES) for d in range(DICE)))
    outcome_counts[throw_sum - 1] += 1

plt.barh(ys, outcome_counts, align='center', alpha=0.4)
plt.xlabel('Number of each outcome')
plt.ylabel('Outcome (Sum of Die Values)')
die_or_dice = "Die" if DICE == 1 else "Dice"
plt.title(f'{die_or_dice} Throw Simulation—{DICE} {SIDES}-Sided {die_or_dice}')
plt.ylim((DICE - 1, highest_outcome + 1))
plt.show()
