from random import randint
print('''
Welcome to the high-low guessing game.
I am thinking of an integer between 1 and 100.
''')

guess = None
guesses = 0
number = randint(1, 100)

while guess != number:
    guesses += 1
    guess = int(input('What is your guess? '))

    if guess > number:
        print('Too high')
    elif guess < number:
        print('Too low')

print('You found the number in', guesses, 'guesses')
