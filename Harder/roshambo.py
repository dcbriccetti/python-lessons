from random import randint

choices = ('rock', 'paper', 'scissors')
beats = (2, 0, 1)

my_choice = randint(0, 2)

player_choice_string = input('rock, paper, or scissors? ')

if player_choice_string in choices:
    player_choice = choices.index(player_choice_string)
    player_beats = beats[player_choice]
    i_beat       = beats[my_choice]

    if player_beats == my_choice:
        print('You win against my ' + choices[my_choice])
    elif i_beat == player_choice:
        print('My %s beats your %s.' % (choices[my_choice], player_choice_string))
    else:
        print('We both chose ' + choices[my_choice])
else:
    print('%s is not one of %s' % (player_choice_string, choices))
