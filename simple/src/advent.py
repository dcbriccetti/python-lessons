import random, sys

transitions = {
    'airstrip': ('forest',),
    'forest': ('airstrip', 'cave'),
    'cave': ('forest', 'meadow'),
    'meadow': ('cave',),
}
places = tuple(transitions.keys())
place = random.choice(places)

while True:
    print('You are at the', place)
    destinations = transitions[place]
    print('From here you can go to', ', '.join(destinations))
    newDest = input('Where would you like to go? ')
    if newDest == 'quit':
        break
    if newDest in destinations:
        if random.randint(1,10) == 1:
            print('You were struck by lightning. Game over.')
            sys.exit()
        place = newDest
        if place == 'meadow':
            if random.randint(1,2) == 1:
                print('You fell in a hole and you are stuck.')
                sys.exit()
            if random.randint(1,2) == 1:
                print('You discover an amazing treasure!')
    else:
        print("You can't go there.")
