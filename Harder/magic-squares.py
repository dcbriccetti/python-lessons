'Finds all 3 by 3 magic squares by brute force'

from itertools import permutations

lines = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
)


def is_magic(permutation):

    def line_sum(line_index):
        return sum((permutation[cell_index] for cell_index in lines[line_index]))

    sum0 = line_sum(0)
    all_but_first = range(1, len(lines))
    return all((line_sum(line_index) == sum0 for line_index in all_but_first))


magic_squares = (p for p in permutations(range(1, 10)) if is_magic(p))

for ms in magic_squares:
    print()
    for i in range(0, 9, 3):
        print(ms[i], ms[i+1], ms[i+2])
