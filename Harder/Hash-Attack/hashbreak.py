from hashlib import md5
from permuter import chars_range, Permuter


def hash_with_md5(string):
    return md5(bytes(string, 'utf-8')).hexdigest()

plaintext = 'zoom'
hashed_secret = hash_with_md5(plaintext)

MAX_STRING_LENGTH = len(plaintext)
CHARS = ''.join(chars_range('a', 'z') + list(' .'))
print(CHARS)

permuter = Permuter(CHARS, MAX_STRING_LENGTH)

for guess in permuter.next():
    hashed_guess = hash_with_md5(guess)
    if hashed_guess == hashed_secret:
        print('Found {:s} in {:,d} tries.'.format(guess, permuter.generated))
        break
