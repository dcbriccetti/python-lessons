'''
Rock, paper scissors game.

Illustrates use of tuples, join, strip, lower, enumerate, randint, custom functions, while, break,
and if/elif/else.
'''

from random import randint

choices = ('rock', 'paper', 'scissors')
beats   = ( 2,      0,       1        )
formatted_choices = ', '.join(choices)

def _index_of_matching(s):
    for index, choice in enumerate(choices):
        if s and choice.startswith(s):
            return index

while True:
    my_choice = randint(0, 2)
    player_choice_string = input(formatted_choices + '? ').strip().lower()
    if not player_choice_string:
        break
    player_choice = _index_of_matching(player_choice_string)

    if player_choice is None:
        print(player_choice_string, 'is not one of', formatted_choices)
    else:
        player_beats = beats[player_choice]
        i_beat       = beats[my_choice]

        if player_beats == my_choice:
            print('You win against my', choices[my_choice])
        elif i_beat == player_choice:
            print('My %s beats your %s.' % (choices[my_choice], choices[player_choice]))
        else:
            print('We both chose', choices[my_choice])
