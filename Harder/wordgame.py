from random import choice

with open('common-words.txt') as file:
    all_words = [line.strip().lower() for line in file if not line.startswith('#')]

words = [choice(all_words) for n in range(10)]

while True:
    letters = input('Letters? ')
    for word in words:
        if letters == word:
            print('You got ' + word)
        for letter in word:
            print(letter if letter in letters else '_', end='')
        print()
