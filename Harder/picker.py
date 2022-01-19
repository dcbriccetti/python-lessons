# This program pops names off a list in random sequence

from random import randint
from time import sleep

remaining_names = 'sue mary hari fred eric menlo'.split()

while remaining_names:
    pop_index = randint(0, len(remaining_names) - 1)
    popped_name = remaining_names.pop(pop_index)
    print(popped_name)
    sleep(1)
