from random import randint
from time import time

print('Enjoy a math quiz, and respond with nothing to stop.')
num_right = 0
num_wrong = 0
total_right_answer_seconds = 0.0

while True:
    num1 = randint(2, 9)
    num2 = randint(11, 99)
    product = num1 * num2
    start_time = time()
    response = input(f'What is {num1} × {num2}? ')
    if not response:
        break
    elapsed = time() - start_time
    try:  # `int` may fail
        if int(response) == product:
            print(f'Right, in {elapsed:.2f} seconds')
            num_right += 1
            total_right_answer_seconds += elapsed
        else:
            print(f'Wrong, the answer was {product}')
            num_wrong += 1
    except ValueError:
        print('You entered something other than an integer')

print(f'You got {num_right} right and {num_wrong} wrong.')
if num_right:
    print(f'Average time for right answers: {total_right_answer_seconds / num_right :.2f} seconds.')
