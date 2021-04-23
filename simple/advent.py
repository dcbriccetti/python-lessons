from random import choice, randint
from typing import List

transitions = {  # Each place, and where you can go from it
    'airstrip': ['forest'],
    'forest':   ['airstrip', 'cave'],
    'cave':     ['forest', 'meadow'],
    'meadow':   ['cave'],
}
places: List[str] = list(transitions.keys())
current_place: str = choice(places)
alive = True
inventory = []

while alive:
    print('You are at the', current_place)
    if inventory:
        print(f"You are carrying: {', '.join(inventory)}")
    destinations: List[str] = transitions[current_place]
    print('From here you can go to', ', '.join(destinations))
    new_place = input('Where would you like to go? ')
    if not new_place:
        print('You have left the game')
        break
    else:
        if new_place in destinations:
            # Things that can happen anywhere
            if randint(1, 10) == 1:
                print('You were struck by lightning. Game over.')
                alive = False
            else:
                current_place = new_place
                # Things that can happen in specific places
                if current_place == 'meadow':
                    if randint(1, 4) == 1:
                        print('You fell in a hole and you are stuck.')
                        alive = False
                    elif randint(1, 3) == 1:
                        print('You discover an amazing treasure!')
                        inventory.append('an amazing treasure')
                elif current_place == 'cave':
                    if randint(1, 2) == 1:
                        print('You have a new pet bat')
                        inventory.append('a bat')
        else:
            print("You can't go there.")
