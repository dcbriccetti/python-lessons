'''Shows how to use if.'''

print('''
Welcome to my exciting game!
Here are the instructions.
Blah, blah.
''')

player = input('What is your name? ')
pl = player.lower()
if pl in ('mom', 'dad'):
    print('Sorry, this game is just for kids')
elif pl == 'sam':
    print('Hello little brother.')
elif pl == 'jean':
    print('Hello little sister.')
elif pl == 'pete':
    print('Hello uncle.')
else:
    print('Nice to meet you,', player)
