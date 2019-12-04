from random import randint
from time import time

print('Enjoy a math quiz, and respond with nothing to stop.')

while True:
    num1 = randint(2, 9)
    num2 = randint(11, 99)
    product = num1 * num2
    start_time = time()
    response = input(f'What is {num1} * {num2}? ')
    if not response:
        break

    try:
        answer = int(response)
        elapsed = time() - start_time
        print(f'Right, in {elapsed:.2f} seconds' if answer == product else f'Wrong, the answer was {product}')
    except ValueError:
        print('You entered something other than an integer')
