from random import choice

items = ('soup', 'corn', 'milk', 'bread', 'eggs')
item = choice(items)
positiveSayings = ('Stay in school!', "Don't do drugs!")

MAX_GUESSES = 3
print('Mr. T says guess the food item in %d guesses.' % MAX_GUESSES)
print('Items: ' + ', '.join(items))

for guessNum in range(MAX_GUESSES):
    guess = input('Your guess? ')
    if guess == item:
        print("That's right. " + choice(positiveSayings))
        break  # Exit the while loop

    print('Wrong.', MAX_GUESSES - guessNum - 1, 'guesses left.')

if guess != item:
    print("I pity the fool!")
