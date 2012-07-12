import random, sys

places = ('airstrip', 'forest', 'cave')
transitions = {
    'airstrip': ('forest',),
    'forest': ('airstrip', 'cave'),
    'cave': ('forest',),
}
place = random.choice(places)

while True:
    print('You are at the ' + place)
    destinations = transitions[place]
    print('From here you can go to ' + ', '.join(destinations))
    newDest = input('Where would you like to go? ')
    if newDest == 'quit':
        break
    if newDest in destinations:
        if random.randint(1,10) == 1:
            print('You were struck by lightning. Game over.')
            sys.exit()
        place = newDest
    else:
        print("You can't go there.")
