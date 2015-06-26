from random import randint
from time import time

print('Enjoy a math quiz, and respond 0 to stop.')

while True:
    m1 = randint(2, 11)
    m2 = randint(2, 11)
    product = m1 * m2
    start_time = time()
    answer = int(input('What is %d * %d ' % (m1, m2)))
    if answer == 0:
        break
        
    if answer == product:
        print('Right, in %.2f seconds' % (time() - start_time))
    else:
        print('Wrong, the answer was %d' % product)
