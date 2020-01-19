simple_plaintext = 'The eagle flies at dawn.'
all_ascii_chars: str = ''.join((chr(n) for n in range(256)))


def shifted_by(ch, shift_by):
    return chr((ord(ch) + shift_by) % 256)


def encrypt(plaintext) -> str:
    return ''.join((shifted_by(ch, 1) for ch in plaintext))


def decrypt(cyphertext) -> str:
    return ''.join((shifted_by(ch, -1) for ch in cyphertext))


if __name__ == '__main__':
    # Test with a simple message, and with a string made of all 8-bit ASCII characters
    for plaintext in (simple_plaintext, all_ascii_chars):
        cyphertext: str = encrypt(plaintext)
        print(cyphertext)
        decoded: str = decrypt(cyphertext)
        print(decoded)
        assert plaintext == decoded
