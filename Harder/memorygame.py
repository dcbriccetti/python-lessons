from random import randint, choice, shuffle
from time import sleep
from typing import Sequence, Optional, Iterator

def clear():
    for n in range(100):  # “Clear” the console
        print()

def create_sequence(
        include: Optional[int] = None,
        exclude: Optional[Iterator[int]] = None) -> Sequence[int]:
    unique_numbers: set[int] = {include} if include else set()
    excluding: set[int] = exclude or set()
    while len(unique_numbers) < seq_length:
        candidate = randint(1, highest_num)
        if candidate not in excluding:
            unique_numbers.add(candidate)
    unique_numbers_list = list(unique_numbers)
    shuffle(unique_numbers_list)
    return unique_numbers_list

seq_length = 3
highest_num = 20

while True:
    first_sequence = create_sequence()
    clear()
    print(f'Remember these numbers:\n{first_sequence}')
    sleep(2)

    number_in_both_sequences = choice(first_sequence)
    second_sequence = create_sequence(include=number_in_both_sequences, exclude=first_sequence)

    clear()
    response = input(f'Which one of these numbers was in the previous sequence?\n{second_sequence}')
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

