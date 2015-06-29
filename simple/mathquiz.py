from random import randint
from time import time

print('Enjoy a math quiz, and respond with nothing to stop.')

while True:
    m1 = randint(2, 11)
    m2 = randint(2, 11)
    product = m1 * m2
    start_time = time()
    response = input('What is %d * %d ' % (m1, m2))
    if response == '':
        break
    answer = int(response)

    if answer == product:
        print('Right, in %.2f seconds' % (time() - start_time))
    else:
        print('Wrong, the answer was %d' % product)
