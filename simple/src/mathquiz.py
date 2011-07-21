from random import randint

print('Enjoy a math quiz, and respond 0 to stop.')

while True:
    m1 = randint(2, 11)
    m2 = randint(2, 11)
    prod = m1 * m2
    ans = int(input('What is {0} * {1} '.format(m1, m2)))
    if ans == 0:
        break
    print('Right' if ans == prod else 'Wrong, the answer was %d' % prod)
