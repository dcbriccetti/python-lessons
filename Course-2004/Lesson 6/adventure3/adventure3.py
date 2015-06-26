# Dave's Exciting Text Adventure Game, Version 3

from place import Place
from placexml import PlaceXml
from commandline import CommandLine

def showDirections():
    directions = ['', '', 'Welcome to',
                  'Dave\'s Exciting Text Adventure Game, now with XML.',
                  '(The X is for eXtra fun!!!)', '']
    for dirLine in directions:
        print(dirLine.center(70))

    print('''
Commands:
    go "place"
    get "object"
    quit
''')
    
def showItems():
    if collectedItems:
        print('You have collected these items:')
        for item in collectedItems:
            print("\t", item)


# Load all the places from the XML file into the places hash
places = {}
placeXml = PlaceXml("game.xml", places)

# Set the starting place, from an attribute in the XML file
place = places[placeXml.startingPlace]

# Keep our collected items in a list
collectedItems = []

showDirections()


keepPlaying = 1

# Create one of these to parse our command lines
commandLine = CommandLine()

# Loop until the user wants to quit
while keepPlaying:
    place.show()
    print()
    showItems()

    # Get a line, and give it to the parser
    rawLine = input('--> ')
    commandLine.set(rawLine)

    if commandLine.cmd == 'go':
        newPlace = commandLine.args
        if newPlace in place.connections:
            # The requested place is valid. "Move" to it.
            place = places[newPlace]
        else:
            print('There\'s no place called "%s," now, is there?' % newPlace)
            
    elif commandLine.cmd == 'get':
        requestedItem = commandLine.args
        if requestedItem in place.objects:
            print('You got the', requestedItem)
            collectedItems.append(requestedItem)
            place.deleteObject(requestedItem)
        else:
            print('There\'s no object called "%s," and everyone knows it.' % requestedItem)

    elif commandLine.cmd == 'quit':
        keepPlaying = 0
        print('Come back real soon, now, you hear?')

    else:
        print('Why would you type something like, "%s"?' % (rawLine))
