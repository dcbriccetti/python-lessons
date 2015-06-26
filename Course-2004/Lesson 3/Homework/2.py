def getRoster():
    roster = []
    print('Enter names, one per line. Give an empty name when done.')
    while 1:
        name = eval(input('==> '))
        if name == "":
            break
        roster.append(name)
    return roster

print('Math class')
mathRoster = getRoster()
print('English class')
englishRoster = getRoster()

print(('Math class:', mathRoster))
print(('English class:', englishRoster))

print('In both classes:')

for name in mathRoster:
    if name in englishRoster:
        print(name)

        
