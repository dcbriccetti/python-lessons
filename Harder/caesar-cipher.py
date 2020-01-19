simple_plaintext = 'The eagle flies at dawn.'
all_ascii_chars: str = ''.join((chr(n) for n in range(256)))


def _shift_character(ch, shift_by) -> str:
    return chr((ord(ch) + shift_by) % 256)


def shift(plaintext, num_positions: int) -> str:
    return ''.join((_shift_character(ch, num_positions) for ch in plaintext))


if __name__ == '__main__':
    # Test with a simple message, and with a string made of all 8-bit ASCII characters
    for plaintext in (simple_plaintext, all_ascii_chars):
        cyphertext: str = shift(plaintext, 1)
        print(cyphertext)
        decoded: str = shift(cyphertext, -1)
        print(decoded)
        assert plaintext == decoded
