import random

# names is a list of names, initally empty
names = []

# Keep looping until no name is entered
while 1:
    name = eval(input('Name: '))

    # If no name given, exit loop with break
    if name == "":
        break

    # Add this name to the list of names
    names.append(name)

# Mix up the list of names with shuffle
random.shuffle(names)

# Display all the shuffled names, one per line
for name in names:
    print(name)
