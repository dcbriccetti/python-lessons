plaintext   = 'meet me at the usual place'
fromLetters = 'abcdefghijklmnopqrstuv0123456789 '
toLetters   = '6n4pde3fs 2c1ivjr05lq8utbgam7hk9o'

for c in plaintext:
    print(toLetters[fromLetters.index(c)], end='')

print()
    
cyphertext = '1ddlo1do6lolfdoq5q6cojc64d'
for c in cyphertext:
    print(fromLetters[toLetters.index(c)], end='')
