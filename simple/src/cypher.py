plaintext   = 'meet me at the usual place'
fromLetters = 'abcdefghijklmnopqrstuv0123456789 '
toLetters   = '6n4pde3fs 2c1ivjr05lq8utbgam7hk9o'

for plaintext_char in plaintext:
    from_letters_index = fromLetters.index(plaintext_char)
    encrypted_letter = toLetters[from_letters_index]
    s = "%s -> %s" % (plaintext_char, encrypted_letter)
    print(s)

print()
    
cyphertext = '1ddlo1do6lolfdoq5q6cojc64d'
for cyphertext_char in cyphertext:
    to_letters_index = toLetters.index(cyphertext_char)
    decrypted_letter = fromLetters[to_letters_index]
    print(decrypted_letter, end='')
