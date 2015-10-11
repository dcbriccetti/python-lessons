'''
Rock, paper scissors game.

Illustrates use of tuples, join, strip, lower, enumerate, randint, custom functions, while, break,
and if/elif/else.
'''

from random import randint

choices = ('rock', 'paper', 'scissors')
formatted_choices = ', '.join(choices)

def _beaten_by(i):
    'Return the index of the choice beaten by the choice with index i'
    return (i + 2) % 3  # Each beats the one to the left of it (wrapping around)

def _index_of_matching_choice(s):
    for index, choice in enumerate(choices):
        if s and choice.startswith(s):
            return index

while True:
    my_choice = randint(0, 2)
    player_choice_string = input(formatted_choices + '? ').strip().lower()
    if not player_choice_string:
        break
    player_choice = _index_of_matching_choice(player_choice_string)

    if player_choice is None:
        print(player_choice_string, 'is not one of', formatted_choices)
    else:
        if my_choice == _beaten_by(player_choice):
            print('You win against my', choices[my_choice])
        elif player_choice == _beaten_by(my_choice):
            print('My %s beats your %s.' % (choices[my_choice], choices[player_choice]))
        else:
            print('We both chose', choices[my_choice])
