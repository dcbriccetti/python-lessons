from random import choice

print('Welcome to Library Adventure')

transitions = {
    'Main Room':   ('Tech Lab', 'Teen Center'),
    'Tech Lab':    ('Main Room',),
    'Teen Center': ('Main Room',),
}
places = tuple(transitions.keys())
place = choice(places)
alive = True

while alive:
    print('You are in the', place)
    destinations = transitions[place]
    print('From here you can go to', ', '.join(destinations))
    new_place = input('Where would you like to go? ')
    if not new_place:
        print('You have left the game')
        break
    else:
        if new_place in destinations:
            place = new_place
        else:
            print("You can't go there.")
