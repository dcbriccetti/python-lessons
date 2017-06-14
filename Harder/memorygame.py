from random import randint, choice, shuffle
from time import sleep

seq_length = 3
highest_num = 20


def clear():
    for n in range(100):  # Clear the console
        print()


while True:
    first_sequence = set()
    while len(first_sequence) < seq_length:
        first_sequence.add(randint(1, highest_num))
    first_sequence = list(first_sequence)
    shuffle(first_sequence)

    clear()
    print('Remember these numbers:')
    print(first_sequence)
    sleep(2)

    number_in_both_sequences = choice(first_sequence)

    second_sequence = set()
    second_sequence.add(number_in_both_sequences)
    while len(second_sequence) < seq_length:
        candidate = randint(1, highest_num)
        if candidate not in first_sequence:
            second_sequence.add(candidate)
    second_sequence = list(second_sequence)
    shuffle(second_sequence)

    clear()
    print('Which one of these numbers was in the previous sequence? ')
    print(second_sequence)

    response = input()
    if not response:
        break
    if response == str(number_in_both_sequences):
        print('Correct')
        seq_length += 1
    else:
        print('Wrong')
        if seq_length > 1:
            seq_length -= 1

    sleep(1)
