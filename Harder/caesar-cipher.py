alphabet = 'abcdefghijklmnopqrstuvwxyz '

plaintext = 'the sparrow flies at midnight'

def encrypt(plaintext):
    ciphertext = ''
    for char in plaintext:
        index = (alphabet.index(char) + 1) % 27
        ciphertext += alphabet[index]
    return ciphertext

print(encrypt(plaintext))
