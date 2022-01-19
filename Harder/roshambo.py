'''
Rock, paper scissors game.

Illustrates use of Enum, tuples, join, strip, lower, enumerate, randint,
custom functions, while, break, and if/elif/else.
'''

from random import choice
from enum import Enum

class Item(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def __str__(self) -> str:
        return self.name.lower()

    def beats(self, item) -> bool:
        'Return the item this item beats'
        # Each beats the item that precedes it (wrapping around)
        beats_value: int = (self.value - 1) % 3
        return item == Item(beats_value)

item_names = [item.name for item in Item]
formatted_items = ', '.join(name.lower() for name in item_names)

while True:
    my_item = choice(list(Item))
    player_item_string = input(formatted_items + '? ').strip()
    if not player_item_string:
        break
    if player_item_string.upper() not in item_names:
        print(player_item_string, 'is not one of', formatted_items)
    else:
        player_item = Item[player_item_string.upper()]
        if player_item.beats(my_item):
            print('You win against my', my_item)
        elif my_item.beats(player_item):
            print(f'My {my_item} beats your {player_item}.')
        else:
            print('We both chose', my_item)
