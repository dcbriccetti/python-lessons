def showPlace():
    print((place[0]))
    objects = place[2]
    if objects:
        print('These objects are here:')
        for object in objects:
            print("\t", object)
    print('From here you can go to: ')
    for otherPlace in place[1]:
        print("\t", otherPlace)

def showItems():
    if collectedItems:
        print('You have collected these items:')
        for item in collectedItems:
            print("\t", item)

places = {}
collectedItems = []
places["forest"] = [
    "You are in the middle of a dark forest. Strange creatures howl in the distance.",
    ("airstrip", "waterfall", "mars"),
    ["acorn", "codebook", "bicycle"]
    ]
places["airstrip"] = [
    "You are at the airstrip. The place is covered with weeds.",
    ("forest",),
    ["propeller"]
    ]
places["waterfall"] = [
    "The waterfall makes a deafening sound.",
    ("forest",),
    ["fish"]
    ]
places["mars"] = [
    "Mars is spacious.",
    ("airstrip",),
    ["rock", "robot junk"]
    ]

place = places["forest"]

while place:
    showPlace()
    showItems()
    cmdLine = input('--> ')
    cmdWords = cmdLine.split(' ')
    cmd = cmdWords[0]
    availPlaces = place[1]
    availItems = place[2]

    if cmd == 'go':
        newPlace = cmdWords[1]
        if newPlace in availPlaces:
            place = places[newPlace]
        else:
            print('You can\'t go there.')
    elif cmd == 'get':
        requestedItem = cmdWords[1]
        if requestedItem in availItems and not (cmdWords[1] in collectedItems):
            collectedItems.append(requestedItem)
