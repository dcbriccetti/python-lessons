from random import choice

items = ['soup', 'corn', 'milk', 'bread', 'eggs']
item = choice(items)
positiveSayings = ['Stay in school!', "Don't do drugs!"]

guess = None
guessesLeft = 3
print(f'Mr. T says guess the food item in {guessesLeft} guesses.')
print('Items:', ', '.join(items))

while guess != item and guessesLeft:
    guess = input('Your guess? ')
    guessesLeft -= 1
    if guess != item and guessesLeft:
        singularOrPlural = 'guess' + ('' if guessesLeft == 1 else 'es')
        print(f'Wrong. {guessesLeft} {singularOrPlural} left.')

if guess == item:
    print("That's right.", choice(positiveSayings))
else:
    print("I pity the fool!")
