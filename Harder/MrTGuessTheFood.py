from random import choice

items = ('soup', 'corn', 'milk', 'bread', 'eggs')
item = choice(items)
positiveSayings = ('Stay in school!', "Don't do drugs!")

guess = ''
guessesLeft = 3
print('Mr. T says guess the food item in %d guesses.' % guessesLeft)
print('Items: ' + ', '.join(items))

while guess != item and guessesLeft > 0:
    guess = input('Your guess? ')
    guessesLeft -= 1
    if guess == item:
        print("That's right. " + choice(positiveSayings))
    elif guessesLeft > 0:
        singularOrPlural = 'guess' if guessesLeft == 1 else 'guesses'
        print('Wrong. %d %s left.' % (guessesLeft, singularOrPlural))

if guess != item:
    print("I pity the fool!")
