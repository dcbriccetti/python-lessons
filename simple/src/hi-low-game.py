import random
print('''
Welcome to the high-low guessing game.
I am thinking of an integer between 1 and 100.
''')

guess = 0
numGuesses = 0
number = random.randint(1, 100)

while guess != number:
    numGuesses += 1
    guess = int(input('What is your guess? '))

    if guess == number:
        print('Congratulations!')
    elif guess > number:
        print('Too high')
    else:
        print('Too low')

print('You found the number in', numGuesses, 'guesses')
