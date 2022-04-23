'Pascal’s Triangle Maker: https://youtu.be/vbr-XaMVTsc'

from itertools import pairwise

def make_triangle(num_rows=10):
    def make_next_row(row: list[int]) -> list[int]:
        return [1] + [left + right for left, right in pairwise(row)] + [1]

    def format_row(row_numbers: list[int]):
        centered_padded_nums: list[str] = [f'{num: ^3}' for num in row_numbers]
        return f"{' '.join(centered_padded_nums): ^40}"

    row = [1]
    for _ in range(num_rows):
        print(format_row(row))
        row = make_next_row(row)

if __name__ == '__main__':
    make_triangle()
