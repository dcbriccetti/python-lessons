from threading import Thread
from time import sleep
from random import random

NUM_COUNTERS = 3
COUNT_TO = 5


def count_and_sleep():
    for n in range(COUNT_TO):
        seconds = random() / 2
        print('%2d. Waiting %.2f seconds.' % (n + 1, seconds))
        sleep(seconds)


print('All in the main thread')
for n in range(NUM_COUNTERS):
    count_and_sleep()

print('')
print('With multiple threads')
for n in range(NUM_COUNTERS):
    thread = Thread(target=count_and_sleep)
    thread.start()
