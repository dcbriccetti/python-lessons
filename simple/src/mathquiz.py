from random import randint

while True:
    m1 = randint(2, 11)
    m2 = randint(2, 11)
    prod = m1 * m2
    ans = int(input('What is %d * %d? ' % (m1, m2)))
    print('Right' if ans == prod else 'Wrong, the answer was %d' % prod)
