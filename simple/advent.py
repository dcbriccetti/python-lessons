from random import choice, randint

transitions = {
    'airstrip': ('forest',),
    'forest':   ('airstrip', 'cave'),
    'cave':     ('forest', 'meadow'),
    'meadow':   ('cave',),
}
places = tuple(transitions.keys())
place = choice(places)
alive = True

while alive:
    print('You are at the', place)
    destinations = transitions[place]
    print('From here you can go to', ', '.join(destinations))
    new_place = input('Where would you like to go? ')
    if not new_place:
        print('You have left the game')
        break
    else:
        if new_place in destinations:
            if randint(1, 10) == 1:
                print('You were struck by lightning. Game over.')
                alive = False
            else:
                place = new_place
                if place == 'meadow':
                    if randint(1, 3) == 1:
                        print('You fell in a hole and you are stuck.')
                        alive = False
                    elif randint(1, 3) == 1:
                        print('You discover an amazing treasure!')
        else:
            print("You can't go there.")
