messages = {
    'sam':   'Hey, little brother!',
    'fred':  'Congrats on the new lawn-mowing job.',
    'betty': "Where's that five dollars you owe me?",
}

names = list(messages.keys())
names.sort()
print(', '.join(names))

name = input('What is your name? ')
nameLower = name.lower()

if nameLower in messages:
    print(messages[nameLower])
else:
    print("I don't know any " + name)
    