# Pops names off a list in random sequence

from random import randint
import time

remaining_names = ['sue', 'mary', 'hari', 'fred', 'eric', 'menlo']

while len(remaining_names) > 0:
    pop_index = randint(0, len(remaining_names) - 1)
    popped_name = remaining_names.pop(pop_index)
    print(popped_name)
    time.sleep(1)
