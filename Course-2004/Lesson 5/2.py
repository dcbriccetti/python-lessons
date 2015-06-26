class Place:

    def __init__(self, desc, targets, objects):
        self.desc = desc
        self.targets = targets
        self.objects = objects

    def show(self):
        print((place.desc))
        self.showObjects()
        self.showTargets()

    def showObjects(self):
        if self.objects:
            print('These objects are here:')
            for object in self.objects:
                print(("\t", object))

    def showTargets(self):
        if self.targets:
            print('From here you can go to: ')
            for target in self.targets:
                print(("\t", target))

def showItems():
    if collectedItems:
        print('You have collected these items:')
        for item in collectedItems:
            print(("\t", item))

places = {}
collectedItems = []

places["forest"] = Place(
    "You are in the middle of a dark forest. Strange creatures howl in the distance.",
    ("airstrip", "waterfall"),
    ["acorn", "codebook", "bicycle"]
    )
places["airstrip"] = Place(
    "You are at the airstrip. The place is covered with weeds.",
    ("forest",),
    ["propeller"]
    )
places["waterfall"] = Place(
    "The waterfall makes a deafening sound.",
    ("forest",),
    ["fish"]
    )

place = places["forest"]

while 1:
    place.show()
    showItems()
    cmdLine = eval(input('--> '))
    cmdWords = cmdLine.split(' ')
    cmd = cmdWords[0]
    cmdArgs = cmdWords[1]
    availPlaces = place.targets
    availItems = place.objects

    if cmd == 'go':
        newPlace = cmdArgs
        if newPlace in availPlaces:
            place = places[newPlace]
        else:
            print('You can\'t go there.')
    elif cmd == 'get':
        requestedItem = cmdArgs
        if requestedItem in availItems and not (cmdArgs in collectedItems):
            collectedItems.append(requestedItem)
