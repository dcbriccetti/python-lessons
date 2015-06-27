# Pops names off a list in random sequence

from random import randint
import time

names = ['sue', 'mary', 'hari', 'fred', 'eric', 'menlo']

while len(names) > 0:
    pop_index = randint(0, len(names) - 1)
    popped_name = names.pop(pop_index)
    print(popped_name)
    time.sleep(1)
