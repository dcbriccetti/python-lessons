from math import sqrt
from turtle import *

def center_equilateral_triangle(x: float, y: float, side_length=300) -> None:
    height = find_equilateral_triangle_height(side_length)
    x_offset = -side_length / 2
    y_offset = -height / 2
    print(f'{side_length=}, {height=}, {x_offset=}, {y_offset=}')

    penup()
    goto(x + x_offset, y + y_offset)
    pendown()

    for _ in range(3):
        fd(side_length)
        lt(360 / 3)

def find_equilateral_triangle_height(side_length: float) -> float:
    base = side_length / 2
    base_squared = base * base
    hypotenuse = side_length
    hyp_squared = hypotenuse * hypotenuse
    # hyp² = base² + height²    Pythagoras!
    # hyp² - base² = height²    Algebra
    # height² = hyp² - base²
    height_squared = hyp_squared - base_squared
    height = sqrt(height_squared)
    return height


center_equilateral_triangle(0, 0, side_length=200)

input('Press enter/return to exit')
